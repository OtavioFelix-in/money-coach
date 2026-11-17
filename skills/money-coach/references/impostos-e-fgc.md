# Impostos sobre investimentos e FGC

> Regras de imposto mudam. Quando uma regra decidir uma escolha da pessoa, confira se
> ainda vale (Receita Federal, CVM, Banco Central) e diga a data da conferência.
> Os valores abaixo valiam em 2026.

## IR regressivo — renda fixa tributada e fundos de longo prazo

| Prazo da aplicação | Alíquota sobre o rendimento |
|---|---|
| até 180 dias | 22,5% |
| 181 a 360 dias | 20% |
| 361 a 720 dias | 17,5% |
| acima de 720 dias | 15% |

Vale para Tesouro Direto, CDB, RDB, LC, debêntures comuns e fundos de renda fixa de longo
prazo. É retido na fonte no resgate (não precisa pagar à parte).

## IOF
Só nos **primeiros 30 dias**: tabela regressiva sobre o rendimento, de 96% no dia 1 até
0% no dia 30. Depois disso, zero. Por isso evite resgatar renda fixa antes de 30 dias.

## Isentos de IR para pessoa física
- Poupança
- LCI e LCA
- CRI e CRA
- Debêntures incentivadas (infraestrutura)
- Rendimentos de FIIs (fundo cumprindo os requisitos)
- Vendas de ações no mercado à vista até **R$ 20 mil por mês** (soma das vendas, não do lucro)

Ao comparar um isento com um tributado, use a taxa equivalente:
`taxa_tributado_equivalente = taxa_isento / (1 − alíquota_IR)` → `calc.py equivalente`.

## Come-cotas (fundos abertos)
Antecipação de IR no último dia útil de **maio e novembro**: 15% (fundos de longo prazo)
ou 20% (curto prazo), cobrado "comendo" cotas. No resgate paga-se a diferença até a
alíquota regressiva. Fundos de ações, FIIs, ETFs e previdência **não** têm come-cotas.

## Renda variável
| Operação | IR sobre o lucro | Observação |
|---|---|---|
| Ações (swing trade) | 15% | Isento se vendas do mês ≤ R$ 20 mil |
| Day trade | 20% | Sem isenção |
| ETFs de renda variável | 15% | Sem isenção dos R$ 20 mil |
| FIIs (venda de cotas) | 20% | Sem isenção |
| Rendimentos de FII | isento (PF, com requisitos) | |

Nesses casos a **própria pessoa** calcula e paga o DARF até o último dia útil do mês
seguinte à venda com lucro. Prejuízo pode ser compensado com lucros futuros do mesmo
tipo de operação. Tudo vai para a declaração anual.

## Investimentos no exterior
Desde 2024 (Lei 14.754/2023): rendimentos de aplicações financeiras no exterior
(ações, ETFs, juros) são tributados em **15%**, apurados uma vez por ano na declaração.
Variação cambial entra na conta; há regras específicas para depósitos em conta no
exterior. Confira o detalhe atual antes de decisões grandes.

## Previdência
- PGBL: dedução de até 12% da renda bruta tributável (declaração completa).
- Tabela regressiva: 35% (até 2 anos) caindo 5 pontos a cada 2 anos, até 10% (acima de
  10 anos). Tabela progressiva: igual à do IR mensal, com retenção de 15% no resgate e
  ajuste na declaração.

## Imposto de renda da pessoa (salário)
O IR sobre salário mudou em 2026 (reforma do IR, com isenção para rendas mensais até
cerca de R$ 5 mil e redução gradual acima disso). Para conta exata de salário líquido,
confira a tabela vigente na Receita Federal.

## FGC — Fundo Garantidor de Créditos

**Cobre**: CDB, RDB, LC, LCI, LCA, LIG, poupança, depósitos em conta corrente.
**Não cobre**: Tesouro Direto (risco é do governo), CRI, CRA, debêntures, fundos de
investimento, ações, FIIs, previdência, cripto.

**Limites**:
- **R$ 250 mil por CPF por instituição** (ou conglomerado financeiro), somando
  principal e rendimentos.
- **Teto global de R$ 1 milhão por CPF**, renovado a cada 4 anos (vale para pagamentos
  feitos pelo FGC dentro desse período).

**Na prática**:
- Acima de R$ 250 mil num mesmo banco/conglomerado, o excedente fica sem garantia →
  divida entre instituições.
- Se o banco quebra, o FGC paga, mas pode levar **semanas a meses** e paga até a data da
  liquidação (os juros prometidos depois disso se perdem). Por isso a reserva de
  emergência não deve ficar toda em banco pequeno.
- Desconfie de "garantido pelo FGC" em produto que não está na lista acima.
