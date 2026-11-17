#!/usr/bin/env python3
"""Calculadora do money-coach. Python 3.8+, sem dependências, sem rede.

Taxas: --taxa-anual, --cdi e --inflacao em % ao ano; juros de dívida em % ao mês.
"""
import argparse
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def brl(v):
    s = f"{abs(v):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return ("-R$ " if v < 0 else "R$ ") + s


def num(v):
    return f"{v:g}".replace(".", ",")


def pct(v, casas=2):
    return f"{v * 100:.{casas}f}%".replace(".", ",")


def mensal(taxa_anual_pct):
    return (1 + taxa_anual_pct / 100) ** (1 / 12) - 1


def ir_regressivo(dias):
    if dias <= 180:
        return 0.225
    if dias <= 360:
        return 0.20
    if dias <= 720:
        return 0.175
    return 0.15


def iof(dias):
    # Tabela regressiva do IOF sobre o rendimento: 96% no dia 1 até 0% no dia 30.
    tabela = [96, 93, 90, 86, 83, 80, 76, 73, 70, 66, 63, 60, 56, 53, 50,
              46, 43, 40, 36, 33, 30, 26, 23, 20, 16, 13, 10, 6, 3, 0]
    return 0.0 if dias >= 30 else tabela[max(dias, 1) - 1] / 100


# ---------- comandos ----------

def cmd_juros(a):
    i = mensal(a.taxa_anual)
    n = int(round(a.anos * 12))
    saldo, aportado = a.inicial, a.inicial
    print(f"{'Ano':>4} {'Aportado':>16} {'Saldo':>16} {'Juros':>16}")
    for m in range(1, n + 1):
        saldo = saldo * (1 + i) + a.mensal
        aportado += a.mensal
        if m % 12 == 0 or m == n:
            print(f"{m / 12:>4.0f} {brl(aportado):>16} {brl(saldo):>16} {brl(saldo - aportado):>16}")
    print(f"\nTotal aportado: {brl(aportado)}  |  Saldo final: {brl(saldo)}  |  Juros: {brl(saldo - aportado)}")
    if a.inflacao is not None:
        real = saldo / (1 + a.inflacao / 100) ** a.anos
        print(f"Em dinheiro de hoje (inflação {num(a.inflacao)}% a.a.): {brl(real)}")
    print("Obs.: não desconta IR nem taxas.")


def cmd_meta(a):
    i = mensal(a.taxa_anual)
    if a.meses:
        n = a.meses
        fv_ini = a.inicial * (1 + i) ** n
        falta = a.alvo - fv_ini
        if falta <= 0:
            print(f"O valor inicial já chega lá: {brl(fv_ini)} em {n} meses.")
            return
        pmt = falta * i / ((1 + i) ** n - 1) if i else falta / n
        print(f"Para juntar {brl(a.alvo)} em {n} meses ({num(a.taxa_anual)}% a.a.), partindo de {brl(a.inicial)}:")
        print(f"  aporte mensal necessário: {brl(pmt)}")
        print(f"  total aportado: {brl(a.inicial + pmt * n)}  |  juros: {brl(a.alvo - a.inicial - pmt * n)}")
    elif a.mensal:
        saldo, n = a.inicial, 0
        while saldo < a.alvo and n < 1200:
            saldo = saldo * (1 + i) + a.mensal
            n += 1
        if saldo < a.alvo:
            print("Não chega à meta em 100 anos com esses valores.")
            return
        print(f"Com {brl(a.mensal)}/mês a {num(a.taxa_anual)}% a.a., partindo de {brl(a.inicial)}:")
        print(f"  chega a {brl(a.alvo)} em {n} meses ({n // 12} anos e {n % 12} meses).")
    else:
        sys.exit("Informe --meses (para saber o aporte) ou --mensal (para saber o prazo).")
    print("Obs.: não desconta IR nem taxas.")


def _simula_dividas(dividas, extra, ordem):
    ds = [dict(d) for d in dividas]
    meses, juros_total, quitadas = 0, 0.0, []
    while any(d["saldo"] > 0.005 for d in ds) and meses < 600:
        meses += 1
        for d in ds:
            if d["saldo"] > 0:
                j = d["saldo"] * d["juros"]
                d["saldo"] += j
                juros_total += j
        disponivel = extra + sum(d["minimo"] for d in ds)
        for d in ds:  # mínimos
            if d["saldo"] > 0:
                p = min(d["minimo"], d["saldo"])
                d["saldo"] -= p
                disponivel -= p
        alvo = [d for d in ds if d["saldo"] > 0.005]
        alvo.sort(key=(lambda d: -d["juros"]) if ordem == "avalanche" else (lambda d: d["saldo"]))
        for d in alvo:  # sobra na dívida prioritária (e na seguinte, se quitar)
            if disponivel <= 0:
                break
            p = min(disponivel, d["saldo"])
            d["saldo"] -= p
            disponivel -= p
        for d in ds:
            if d["saldo"] <= 0.005 and d["nome"] not in [q[0] for q in quitadas]:
                d["saldo"] = 0
                quitadas.append((d["nome"], meses))
    return meses, juros_total, quitadas, any(d["saldo"] > 0.005 for d in ds)


def cmd_dividas(a):
    dividas = []
    for s in a.divida:
        try:
            nome, saldo, juros, minimo = s.split(":")
            dividas.append({"nome": nome, "saldo": float(saldo), "juros": float(juros) / 100, "minimo": float(minimo)})
        except ValueError:
            sys.exit(f"Formato inválido: {s!r}. Use Nome:saldo:juros_ao_mes:parcela_minima")
    for d in dividas:
        if d["minimo"] <= d["saldo"] * d["juros"]:
            print(f"ATENÇÃO: a parcela de {d['nome']} ({brl(d['minimo'])}) não cobre nem os juros do mês "
                  f"({brl(d['saldo'] * d['juros'])}). Essa dívida só cresce.")
    print(f"Pagamento total por mês: {brl(sum(d['minimo'] for d in dividas) + a.extra)} "
          f"(mínimos + {brl(a.extra)} extra)\n")
    for ordem, desc in (("avalanche", "maior juros primeiro"), ("bola-de-neve", "menor saldo primeiro")):
        meses, juros, quitadas, sobrou = _simula_dividas(dividas, a.extra, ordem)
        print(f"== {ordem} ({desc})")
        if sobrou:
            print("   Não quita em 50 anos: o pagamento não vence os juros. Precisa renegociar ou aumentar o valor.")
            continue
        print(f"   Livre das dívidas em {meses} meses  |  juros pagos: {brl(juros)}")
        print("   Ordem de quitação: " + ", ".join(f"{n} (mês {m})" for n, m in quitadas))


def cmd_financiamento(a):
    i = mensal(a.taxa_anual)
    n, pv = a.meses, a.valor
    pmt = pv * i / (1 - (1 + i) ** -n)
    price_total = pmt * n
    amort = pv / n
    sac_primeira = amort + pv * i
    sac_ultima = amort + amort * i
    sac_juros = sum((pv - amort * k) * i for k in range(n))
    print(f"Financiamento de {brl(pv)} em {n} meses a {num(a.taxa_anual)}% a.a. ({pct(i, 4)} a.m.)\n")
    print(f"PRICE  parcela fixa: {brl(pmt)}  |  total pago: {brl(price_total)}  |  juros: {brl(price_total - pv)}")
    print(f"SAC    1ª parcela: {brl(sac_primeira)}  ->  última: {brl(sac_ultima)}  |  total pago: {brl(pv + sac_juros)}  |  juros: {brl(sac_juros)}")
    print(f"\nSAC economiza {brl(price_total - pv - sac_juros)} em juros.")
    print("Obs.: sem seguros, taxas e correção (TR/IPCA). Use o CET do banco para a conta real.")


def cmd_rendafixa(a):
    taxa_anual = a.cdi / 100 * a.pct_cdi / 100 if a.pct_cdi else a.taxa_anual / 100
    bruto = a.valor * ((1 + taxa_anual) ** (a.dias / 365) - 1)
    rend_iof = bruto * iof(a.dias)
    base_ir = bruto - rend_iof
    ir = 0 if a.isento else base_ir * ir_regressivo(a.dias)
    liquido = bruto - rend_iof - ir
    print(f"{brl(a.valor)} por {a.dias} dias a {pct(taxa_anual)} a.a.{' (isento de IR)' if a.isento else ''}")
    print(f"  rendimento bruto: {brl(bruto)}")
    if rend_iof:
        print(f"  IOF (resgate antes de 30 dias): -{brl(rend_iof)}")
    if not a.isento:
        print(f"  IR ({pct(ir_regressivo(a.dias), 1)}): -{brl(ir)}")
    print(f"  rendimento líquido: {brl(liquido)}  ->  saldo final {brl(a.valor + liquido)}")
    liq_anual = (1 + liquido / a.valor) ** (365 / a.dias) - 1
    print(f"  rentabilidade líquida: {pct(liq_anual)} ao ano")
    if a.inflacao is not None:
        real = (1 + liq_anual) / (1 + a.inflacao / 100) - 1
        print(f"  ganho real (inflação {num(a.inflacao)}% a.a.): {pct(real)} ao ano")


def cmd_equivalente(a):
    ir = ir_regressivo(a.dias)
    eq = a.pct_isento / (1 - ir)
    print(f"Um isento (LCI/LCA) a {num(a.pct_isento)}% do CDI por {a.dias} dias equivale a um tributado "
          f"(CDB/Tesouro) a {num(round(eq, 1))}% do CDI (IR de {pct(ir, 1)}).")
    if a.pct_tributado:
        melhor = "o tributado" if a.pct_tributado > eq else "o isento" if a.pct_tributado < eq else "nenhum (empate)"
        print(f"Comparando com {num(a.pct_tributado)}% do CDI tributado: melhor é {melhor}.")


def cmd_taxa(a):
    if a.mensal is not None:
        anual = (1 + a.mensal / 100) ** 12 - 1
        print(f"{num(a.mensal)}% ao mês = {pct(anual)} ao ano (juros compostos).")
    else:
        m = mensal(a.anual)
        print(f"{num(a.anual)}% ao ano = {pct(m, 4)} ao mês (juros compostos).")


def main():
    p = argparse.ArgumentParser(description="Calculadora do money-coach")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("juros", help="juros compostos com aportes mensais")
    s.add_argument("--inicial", type=float, default=0)
    s.add_argument("--mensal", type=float, default=0)
    s.add_argument("--taxa-anual", type=float, required=True)
    s.add_argument("--anos", type=float, required=True)
    s.add_argument("--inflacao", type=float)
    s.set_defaults(f=cmd_juros)

    s = sub.add_parser("meta", help="aporte mensal para uma meta, ou prazo com um aporte")
    s.add_argument("--alvo", type=float, required=True)
    s.add_argument("--inicial", type=float, default=0)
    s.add_argument("--taxa-anual", type=float, required=True)
    s.add_argument("--meses", type=int)
    s.add_argument("--mensal", type=float)
    s.set_defaults(f=cmd_meta)

    s = sub.add_parser("dividas", help="avalanche x bola de neve")
    s.add_argument("--divida", action="append", required=True, help="Nome:saldo:juros_ao_mes:parcela_minima")
    s.add_argument("--extra", type=float, default=0, help="valor além dos mínimos, por mês")
    s.set_defaults(f=cmd_dividas)

    s = sub.add_parser("financiamento", help="Price x SAC")
    s.add_argument("--valor", type=float, required=True)
    s.add_argument("--taxa-anual", type=float, required=True)
    s.add_argument("--meses", type=int, required=True)
    s.set_defaults(f=cmd_financiamento)

    s = sub.add_parser("rendafixa", help="rendimento líquido de renda fixa (IR e IOF)")
    s.add_argument("--valor", type=float, required=True)
    s.add_argument("--dias", type=int, required=True)
    g = s.add_mutually_exclusive_group(required=True)
    g.add_argument("--pct-cdi", type=float, help="ex.: 110 para 110%% do CDI (exige --cdi)")
    g.add_argument("--taxa-anual", type=float, help="taxa prefixada em %% a.a.")
    s.add_argument("--cdi", type=float, help="CDI atual em %% a.a.")
    s.add_argument("--isento", action="store_true", help="LCI, LCA, CRI, CRA, poupança...")
    s.add_argument("--inflacao", type=float)
    s.set_defaults(f=cmd_rendafixa)

    s = sub.add_parser("equivalente", help="LCI/LCA x CDB: taxa equivalente")
    s.add_argument("--pct-isento", type=float, required=True)
    s.add_argument("--dias", type=int, required=True)
    s.add_argument("--pct-tributado", type=float)
    s.set_defaults(f=cmd_equivalente)

    s = sub.add_parser("taxa", help="converte juros ao mês <-> ao ano")
    g = s.add_mutually_exclusive_group(required=True)
    g.add_argument("--mensal", type=float)
    g.add_argument("--anual", type=float)
    s.set_defaults(f=cmd_taxa)

    a = p.parse_args()
    if a.cmd == "rendafixa" and a.pct_cdi and a.cdi is None:
        p.error("--pct-cdi precisa de --cdi")
    a.f(a)


if __name__ == "__main__":
    main()
