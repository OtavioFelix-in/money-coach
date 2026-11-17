# Dívidas

## Ranking de custo (do mais caro ao mais barato, em geral)

| Dívida | Custo típico | O que fazer |
|---|---|---|
| Agiota | absurdo, e risco físico | prioridade máxima; procure Defensoria/polícia se houver ameaça |
| Rotativo do cartão | os mais altos do país (ao mês) | sair na hora; nunca pagar só o mínimo |
| Cheque especial | teto de 8% ao mês | trocar por crédito mais barato |
| Crédito pessoal sem garantia | alto | renegociar / portabilidade |
| Parcelamento de fatura | alto, mas menor que o rotativo | melhor que rotativo |
| Consignado | baixo | bom para trocar dívida cara |
| Crédito com garantia (veículo/imóvel) | baixo | barato, mas o bem fica em risco |
| Financiamento imobiliário | mais baixo | normalmente não é urgência |

Sempre peça os juros **ao mês** e o **CET** (Custo Efetivo Total, que inclui tarifas,
seguros e IOF — o banco é obrigado a informar). Para converter: `calc.py taxa --mensal X`.

## Regras que protegem a pessoa
- **Rotativo do cartão**: só pode ser usado por um mês; depois o banco tem de oferecer
  parcelamento. Desde 2024, juros e encargos do rotativo/parcelamento da fatura não podem
  passar de **100% do valor original** da dívida.
- **Cheque especial**: juros limitados a **8% ao mês**.
- **Portabilidade de crédito**: a pessoa pode levar a dívida para outro banco com juros
  menores, sem custo; o banco atual pode fazer contraproposta. Funciona para empréstimo
  pessoal, consignado, financiamentos.
- **Amortização antecipada**: pagar antes dá direito a desconto proporcional dos juros.
- **Nome negativado**: o registro em cadastro de inadimplentes (Serasa, SPC) só pode
  ficar até **5 anos**. Isso não apaga a dívida em si; renegociar costuma sair mais barato.
- **Superendividamento** (Lei 14.181/2021): quem não consegue pagar sem comprometer o
  mínimo para viver pode pedir repactuação de todas as dívidas juntas (Procon,
  Defensoria, Justiça).
- Feirões e plataformas oficiais de renegociação (Serasa Limpa Nome, mutirões do
  Banco Central/Procons, programas do governo quando houver) dão descontos grandes.

## Plano de saída

1. **Liste tudo** no `DIVIDAS.md`: credor, saldo, juros ao mês, parcela, atraso.
2. **Corte o sangramento**: parar de usar o cartão que está no rotativo; tirar o limite
   do cheque especial se ele virou "salário extra".
3. **Pague o mínimo de todas** para não gerar multa.
4. **Sobra vai para uma dívida só**:
   - **Avalanche**: maior juros primeiro — paga menos juros no total (matematicamente melhor).
   - **Bola de neve**: menor saldo primeiro — vitória rápida, ajuda quem desanima fácil.
   - Mostre os dois com `calc.py dividas` e deixe a pessoa escolher; a diferença
     costuma ser pequena se os juros são parecidos e grande se há rotativo no meio.
5. **Troque dívida cara por barata** quando possível (consignado, portabilidade,
   empréstimo com garantia — com cuidado, porque o bem fica em risco).
6. **Negocie** à vista com desconto se houver dinheiro; parcelado, só se a parcela couber
   de verdade no orçamento (uma renegociação que quebra de novo piora o histórico).
7. Depois de quitar: **o valor da parcela vira aporte** da reserva.

## Financiamento: Price × SAC

- **Price**: parcelas iguais; no começo paga quase só juros. Total de juros maior.
- **SAC**: amortização constante; parcelas começam mais altas e caem. Total de juros menor.
- Compare com `calc.py financiamento`. SAC costuma ser melhor para quem aguenta a
  parcela inicial.
- Amortização extra: escolher **reduzir o prazo** economiza mais juros que reduzir a parcela.

## Cartão de crédito usado direito
- Pague a **fatura inteira**, sempre. Se não dá, o cartão está sendo usado como empréstimo.
- "Parcelado sem juros" ainda compromete a renda dos próximos meses: some as parcelas
  futuras no `ORCAMENTO.md`.
- Limite alto não é dinheiro. Milhas e cashback não compensam juros.
