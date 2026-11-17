# Investimentos no Brasil — produtos

Para impostos e garantia do FGC, veja `impostos-e-fgc.md`. Para como montar a carteira,
veja `estrategia.md`. Taxas citadas aqui são **exemplos**; para conta real, use
`MERCADO.md` da pessoa (valor atual, com data e fonte).

## Conceitos que a pessoa precisa entender primeiro

- **Selic**: taxa básica de juros, definida pelo Copom a cada ~45 dias. Puxa quase toda
  a renda fixa.
- **CDI**: taxa dos empréstimos entre bancos; anda colada na Selic (um pouco abaixo).
  "100% do CDI" ≈ rende a Selic.
- **IPCA**: inflação oficial. **Ganho real** = rendimento acima da inflação.
  Fórmula: `(1 + rendimento) / (1 + inflação) − 1`.
- **Liquidez**: em quanto tempo vira dinheiro na conta sem perder valor.
- **Risco de crédito**: o emissor não pagar. **Risco de mercado**: o preço oscilar antes
  do vencimento.
- **Marcação a mercado**: título vendido antes do vencimento sai pelo preço do dia, que
  pode ser maior ou menor que o investido. Levado até o vencimento, paga o combinado.
- **Pós-fixado** (% do CDI, Selic): acompanha os juros. **Prefixado**: taxa travada.
  **Híbrido** (IPCA + X%): inflação mais uma taxa fixa.

## Renda fixa

### Tesouro Direto (títulos públicos federais)
Risco do governo federal — o menor do país. **Não tem FGC (não precisa)**. Compra pelo
app/site de corretora ou banco, a partir de ~R$ 30. Liquidez diária (D+0/D+1) vendendo
para o Tesouro, pelo preço do dia. Paga IR regressivo e taxa de custódia da B3
(pequena; confira o valor atual e as isenções).

| Título | Rende | Melhor uso | Cuidado |
|---|---|---|---|
| **Tesouro Selic** | Selic | Reserva de emergência, curto prazo | Quase não oscila; IR regressivo pune resgate cedo |
| **Tesouro Prefixado** | Taxa fixa | Meta com data, quando se acha que os juros vão cair | Oscila; vender antes pode dar perda |
| **Tesouro Prefixado com juros semestrais** | Taxa fixa, paga cupons | Renda periódica | Cupom é tributado a cada pagamento |
| **Tesouro IPCA+** | Inflação + taxa fixa | Longo prazo, aposentadoria, proteção da inflação | Oscila bastante; para levar até o vencimento |
| **Tesouro IPCA+ com juros semestrais** | IPCA + taxa, paga cupons | Renda periódica corrigida | Cupons tributados; reinvestimento |
| **Tesouro RendA+** | Renda mensal corrigida pelo IPCA por 20 anos, a partir da data escolhida | Complemento de aposentadoria | Oscila muito antes da conversão; regras de resgate antecipado |
| **Tesouro Educa+** | Renda mensal por 5 anos, para estudo | Faculdade de filho | Mesmo cuidado do RendA+ |

### CDB, RDB, LC (bancos e financeiras)
Empréstimo ao banco. **Coberto pelo FGC** até o limite (ver `impostos-e-fgc.md`).
- Pós (% do CDI), pré ou IPCA+.
- **Liquidez diária** existe em vários (bom para reserva); com carência costuma pagar mais.
- Banco menor costuma pagar mais (110%–130% do CDI) por ter risco maior — o FGC cobre
  até o limite, mas o resgate pode demorar meses se o banco quebrar. Não use banco
  pequeno sem liquidez para a reserva inteira.
- IR regressivo; IOF nos primeiros 30 dias.

### LCI e LCA (Letras de Crédito Imobiliário / do Agronegócio)
- **Isentas de IR para pessoa física** e cobertas pelo FGC.
- Têm **carência mínima** obrigatória (desde 2024 é de vários meses — confira a regra
  vigente); não servem para reserva de emergência.
- Para comparar com CDB, use a taxa equivalente: `calc.py equivalente`. Ex.: LCI a 92%
  do CDI por 400 dias equivale a um CDB a ~111% do CDI (IR de 17,5%).
- A isenção já foi alvo de propostas de mudança; confirme se ainda vale.

### CRI, CRA e debêntures
Dívida de empresas (imobiliário, agronegócio, infraestrutura). CRI/CRA e **debêntures
incentivadas** são isentos de IR para PF.
- **Sem FGC**. O risco é a empresa — confira rating, setor e a concentração.
- Liquidez baixa: venda antes do vencimento pode sair com deságio.
- Para quem já tem reserva e uma base de Tesouro/CDB; não para iniciantes.

### Poupança
- Isenta de IR, coberta pelo FGC, liquidez imediata.
- Regra: com Selic **acima de 8,5% ao ano**, rende **0,5% ao mês + TR**; com Selic até
  8,5%, rende **70% da Selic + TR**.
- Rende no "aniversário" mensal: tirar antes perde o mês.
- Com Selic alta, costuma perder para Tesouro Selic e CDB de liquidez diária a 100% do CDI
  mesmo depois do IR. Mostre a conta.

## Fundos de investimento
Gestor profissional, mas com **taxa de administração** (e às vezes de performance) que
come o rendimento todo ano. Fundos de renda fixa e multimercado abertos têm
**come-cotas**. Regra prática: fundo DI/renda fixa simples com taxa acima de ~0,5% ao ano
quase nunca compensa frente a Tesouro/CDB diretos. Olhe: taxa, histórico vs. CDI em
vários anos, prazo de resgate (D+30 não serve para reserva), tamanho e gestora.

## Renda variável

### Ações
Pedaço de empresa. Ganha com valorização e dividendos/JCP. Volátil: quedas de 30%–50%
acontecem. Só com dinheiro que pode ficar **5 anos ou mais** sem ser usado.
- Diversifique (vários setores) ou use ETF.
- Isenção de IR em vendas de até **R$ 20 mil por mês** (ações, mercado à vista; não vale
  para ETF nem FII).
- Day trade: a grande maioria das pessoas perde dinheiro. Não é renda.

### ETFs (fundos de índice)
Compram uma cesta inteira (ex.: Ibovespa, S&P 500) num papel só. Diversificação barata,
taxa baixa. Bom ponto de partida em renda variável. Tributação de 15% no ganho, sem a
isenção dos R$ 20 mil.

### FIIs (fundos imobiliários)
Imóveis ou papéis imobiliários em cotas negociadas na bolsa. Pagam rendimentos mensais,
em geral isentos de IR para PF quando o fundo cumpre requisitos (número mínimo de
cotistas, cotas em bolsa, participação limitada da pessoa). Ganho na venda: 20%.
- Tijolo (imóveis físicos) × papel (CRIs) × fundos de fundos.
- Rendimento alto demais costuma esconder risco (vacância, inadimplência, CRI ruim).
- A cota oscila como ação.

### BDRs e investimento no exterior
BDR é um recibo, negociado na B3, de ação estrangeira. Também dá para investir lá fora
direto por corretora internacional (regras de IR próprias — `impostos-e-fgc.md`).
Benefício: diversificar moeda e país. Risco: câmbio.

## Previdência privada (PGBL e VGBL)
- **PGBL**: deduz até **12% da renda bruta tributável** do IR, só para quem faz a
  declaração **completa** e contribui para a previdência oficial (INSS ou regime
  próprio). No resgate, o IR incide sobre **tudo** (aporte + rendimento).
- **VGBL**: não deduz; IR só sobre o rendimento. Para quem declara no simplificado ou
  já usou os 12%.
- **Tabela regressiva** (vai de 35% até 10% após 10 anos) ou **progressiva** (tabela do
  IR mensal). Confira as regras atuais sobre o momento de escolher a tabela.
- Vantagens: sucessão (não entra em inventário em muitos casos), sem come-cotas.
- **Cuidado**: taxa de carregamento e de administração altas destroem o plano. Bom plano
  tem carregamento zero e taxa baixa. Previdência vendida no gerente "porque é segura"
  costuma ser cara.

## Criptomoedas
Muito voláteis (quedas de 70%+ já aconteceram várias vezes) e cheias de golpes. Se a
pessoa quiser, só uma **fatia pequena** do patrimônio, depois da reserva, em exchange
ou ETF regulado — nunca "plataforma que rende X% ao mês". As regras de IR para cripto
vêm mudando; confira a vigente.

## Produtos que quase nunca valem como investimento
- **Título de capitalização**: devolve menos que a inflação; é sorteio, não investimento.
- **Consórcio**: pode servir para comprar um bem sem juros (com taxa de administração),
  mas não é investimento.
- **Seguro de vida "com resgate"**, previdência cara, COE complexo vendido pelo gerente:
  analise as taxas antes.
- **Qualquer coisa com retorno "garantido" alto** (ex.: 3% ao mês) — ver golpes em
  `estrategia.md`.

## Como comparar duas opções (roteiro)

1. Mesmo prazo e mesma liquidez? Se não, não são comparáveis direto.
2. Rendimento **líquido** (após IR e taxas) — `calc.py rendafixa` / `equivalente`.
3. **Real** (após inflação), quando o prazo for longo.
4. Risco: FGC? Governo? Empresa? Oscila?
5. Serve para o **objetivo** da pessoa? Isso decide mais do que 5% a mais de CDI.
