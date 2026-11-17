# Estratégia financeira

O produto importa menos que a estratégia. Uma pessoa com Tesouro Selic e aporte todo mês
vence quem caça "o investimento que mais rende" e resgata no pânico.

## 1. A pergunta que vem antes de tudo

**"Para que é esse dinheiro e quando você vai precisar dele?"**

Cada objetivo tem prazo; cada prazo tem um tipo de produto:

| Prazo do objetivo | Prioridade | Produtos que combinam | Evite |
|---|---|---|---|
| **Reserva / a qualquer momento** | liquidez e segurança | Tesouro Selic, CDB liquidez diária ≥ 100% CDI de banco sólido | ações, IPCA+ longo, carência |
| **Até 2 anos** (viagem, carro, curso) | não perder valor | pós-fixados (Tesouro Selic, CDB, LCI/LCA com vencimento antes da data) | renda variável |
| **2 a 5 anos** (entrada de imóvel, casamento) | travar ganho | prefixado ou IPCA+ com **vencimento perto da data**, CDB/LCI/LCA | ações como parte grande |
| **5 anos ou mais** (aposentadoria, independência) | crescer acima da inflação | IPCA+ longo, ações/ETFs, FIIs, exterior, previdência barata | deixar tudo no pós-fixado para sempre |

Regra de ouro: **o vencimento do título deve casar com a data do objetivo**. Assim a
oscilação do meio do caminho não importa.

## 2. Perfil de risco (na prática)

Mais importante que o questionário do banco é a pergunta: "se cair 20%, você vende?"

- **Conservador**: vende no pânico ou perde o sono → quase tudo em renda fixa; renda
  variável só pequena (0–10%) e depois de aprender.
- **Moderado**: aguenta oscilação se entende o motivo → 10–35% em renda variável no longo prazo.
- **Arrojado**: aguenta quedas de 30%+ sem mexer, prazo longo, renda estável → pode ir além.

Perfil também depende de **capacidade** (renda estável? dependentes? reserva pronta?),
não só de vontade. Pessoa sem reserva não tem perfil arrojado, por mais que queira.

## 3. Montando a carteira de longo prazo (modelo didático)

Não é recomendação fixa; é um ponto de partida para discutir com a pessoa:

| Classe | Conservador | Moderado | Arrojado |
|---|---|---|---|
| Pós-fixado (Selic/CDI) | 50% | 25% | 10% |
| Inflação (IPCA+) e prefixado | 40% | 35% | 25% |
| Ações/ETFs Brasil | 5% | 15% | 25% |
| FIIs | 5% | 10% | 10% |
| Exterior (ETFs/BDRs) | 0% | 15% | 25% |
| Cripto (opcional) | 0% | 0–2% | 0–5% |

A reserva de emergência fica **fora** dessa conta.

Princípios:
- **Diversificar** entre classes, emissores (respeitando o FGC) e países.
- **Custos baixos**: taxa de 2% ao ano come ~20% do patrimônio em 20 anos.
- **Simplicidade**: 3–6 produtos bem escolhidos > 25 produtos que a pessoa não entende.

## 4. Aportes, juros compostos e constância

- O motor do patrimônio no começo é o **aporte**, não a rentabilidade. Com R$ 5 mil
  investidos, 1% a mais de rendimento dá R$ 50 por ano; aumentar o aporte em R$ 100/mês
  dá R$ 1.200.
- Mostre o efeito do tempo com `calc.py juros`: ex. R$ 500/mês a 6% real ao ano por 30
  anos ≈ R$ 487 mil em valores de hoje (R$ 180 mil aportados, o resto é juros).
- **Pague-se primeiro**: o aporte sai no dia do salário, automático, não "o que sobrar".
- **Aumento de salário**: direcione pelo menos metade do aumento ao aporte antes que vire
  padrão de vida (inflação de estilo de vida).
- **Aporte mensal > acertar o momento**: ninguém acerta o fundo do poço com constância.

## 5. Rebalanceamento

Uma ou duas vezes por ano, compare a carteira com o alvo. Se uma classe passou muito do
alvo (ex.: +5 pontos), direcione os novos aportes para as que ficaram para trás. Vender
só se o desvio for grande — lembrando IR e a isenção de R$ 20 mil em ações.

## 6. Independência financeira e aposentadoria

- **Número da independência** (aproximação): `gasto mensal desejado × 12 ÷ taxa de
  retirada real`. Com 4% ao ano: gasto × 300. Ex.: R$ 5.000/mês → R$ 1,5 milhão.
  No Brasil, com juros reais historicamente maiores, há quem use 4–5%, mas seja
  conservador e trate como estimativa.
- Use `calc.py meta` para ver quanto aportar por mês até lá.
- Considere o INSS (ou regime próprio) como piso de renda, não como plano todo.
- Quanto mais perto da data, mais renda fixa casada com o prazo (ex.: IPCA+, RendA+).

## 7. Decisões clássicas (com a conta)

- **Quitar dívida ou investir?** Compare a taxa da dívida (ao ano, efetiva) com o
  rendimento **líquido** do investimento. Dívida mais cara → quite. Rotativo e cheque
  especial: sempre quite primeiro.
- **Amortizar financiamento imobiliário ou investir?** Se o investimento líquido rende
  mais que o custo efetivo do financiamento (com seguros e TR/IPCA), investir tende a
  vencer; senão, amortize — de preferência **reduzindo prazo** (economiza mais juros).
- **Comprar à vista com desconto ou parcelar sem juros?** Compare o desconto com o que o
  dinheiro renderia no período. Desconto de 5% à vista quase sempre vence parcelar em 10x.
- **Alugar ou comprar imóvel?** Compare aluguel + rendimento do dinheiro da entrada com
  juros do financiamento + custos (ITBI, escritura, manutenção, IPTU). Não há resposta
  universal; mostre a conta e os fatores não financeiros.
- **Carro**: deprecia ~10–20% ao ano. Financiar carro é pagar juros sobre algo que perde
  valor. Considere o custo total por mês (parcela, seguro, IPVA, manutenção, combustível).

## 8. Armadilhas comportamentais

- **Vender no pânico** depois de uma queda — transforma oscilação em perda.
- **Correr atrás do que subiu** ("todo mundo está ganhando com X").
- **Excesso de confiança** depois de alguns acertos.
- **Concentração**: tudo em uma ação, um banco pequeno, um imóvel.
- **Viés do presente**: adiar o começo "para o mês que vem".
- **Contabilidade mental**: ter dívida de cartão e dinheiro "guardado para outra coisa".

## 9. Golpes e pirâmides — sinais de alerta

Avise com clareza se aparecer:
- Retorno **garantido** e alto (ex.: 2–10% ao mês) ou "sem risco".
- Ganho por **trazer outras pessoas** (indicação, níveis, "rede").
- Pressão de tempo ("só hoje", "últimas vagas").
- Empresa/"trader" sem registro na **CVM** ou no **Banco Central** (consulte nos sites
  oficiais), contato por WhatsApp/Instagram, "robô de trade", "arbitragem de cripto".
- Pedido de Pix para pessoa física, de senha, de código ou de acesso remoto.

Se a pessoa já caiu: parar de mandar dinheiro, guardar provas, registrar boletim de
ocorrência, avisar o banco (MED do Pix, em até poucos dias, ajuda a tentar o
reembolso) e denunciar à CVM. Não "recupere" pagando taxa a quem promete recuperar.
