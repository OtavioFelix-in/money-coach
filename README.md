<p align="center">
  <img src="assets/capa.svg" alt="money-coach: mascote laranja de terno e gravata segurando uma maleta, com moedas subindo e um gráfico crescendo" width="100%">
</p>

<p align="center">
  <img alt="versão" src="https://img.shields.io/badge/vers%C3%A3o-0.1.0-F2C14E?style=flat-square">
  <img alt="comando" src="https://img.shields.io/badge/comando-%2Fmoney--coach%3Amoney--coach-1C2B45?style=flat-square">
  <img alt="idioma" src="https://img.shields.io/badge/idioma-PT--BR-1F7A3A?style=flat-square">
  <img alt="licença" src="https://img.shields.io/badge/licen%C3%A7a-MIT-2EA043?style=flat-square">
  <img alt="feito para" src="https://img.shields.io/badge/feito%20para-Claude%20Code-D97757?style=flat-square">
</p>

<p align="center"><b>Um conselheiro financeiro dentro do Claude Code.</b><br>
Forte em investimentos e estratégia, anota tudo numa pasta sua e não concorda com loucura só porque você insistiu.</p>

---

## O problema

Pergunte de dinheiro a uma IA qualquer e você recebe três coisas: uma lista genérica ("faça um orçamento, tenha uma reserva"), conselhos pensados para os Estados Unidos (401k, IRA, *high-yield savings*) e, se você insistir um pouco, um "você tem razão!" para qualquer ideia. Na conversa seguinte, ela já esqueceu tudo.

O money-coach foi feito para o contrário:

| | IA genérica | Com o money-coach |
|---|---|---|
| **Memória** | esquece tudo a cada conversa | anota renda, dívidas, metas e decisões numa pasta sua |
| **País** | 401k, IRA, dólar | Tesouro, CDB, LCI/LCA, FGC, IR regressivo, come-cotas, rotativo |
| **Conselho** | "invista com sabedoria" | contas com os seus números: quanto rende líquido, quanto custa a dívida, em quantos meses chega |
| **Pressão** | "tem razão, vai fundo!" | respeita que o dinheiro é seu, mas só muda de opinião com fato novo, nunca com insistência |

Exemplo: você recebe R$ 3.000 e quer gastar tudo numa caixa de cartas, deixando as contas para o mês que vem. Ele não proíbe nem dá sermão. Mostra quanto isso vira em multa e juros e oferece um jeito de comprar em três meses sem atrasar nada. Se você pedir "só concorda comigo", a resposta continua sendo a conta.

## O que acontece

<p align="center">
  <img src="assets/fluxo.svg" alt="Sua pasta, entrevista, diagnóstico, plano e acompanhamento: cinco etapas, você cria a pasta, responde e decide" width="100%">
</p>

1. **Sua pasta.** Você cria uma pasta e abre o Claude Code nela. Tudo o que importa fica ali, em arquivos que você pode ler e editar.
2. **Entrevista curta.** Renda, gastos, dívidas, o que já tem guardado, objetivos e como você reage quando um investimento cai. Poucas perguntas por vez.
3. **Diagnóstico.** Sobra do mês, taxa de poupança, quanto da renda vai para dívidas e quantos meses de reserva você tem, com os seus números.
4. **Plano, um degrau por vez.** Parar de afundar, sair das dívidas caras, montar a reserva e investir para cada objetivo, cada um no prazo certo.
5. **Acompanha.** Nas próximas conversas ele lê a pasta e continua de onde parou.

## O que ele sabe

| Assunto | O que cobre |
|---|---|
| **Investimentos** | Tesouro Selic, Prefixado, IPCA+, RendA+ e Educa+; CDB, LCI, LCA, CRI, CRA, debêntures; poupança; fundos; ações, ETFs, FIIs, BDRs, exterior; previdência PGBL e VGBL; cripto |
| **Impostos e garantias** | IR regressivo, IOF, come-cotas, isenções, isenção de R$ 20 mil em ações, investimentos no exterior, FGC e seus limites |
| **Estratégia** | produto certo para cada prazo, perfil de risco, carteira por classe, aportes e juros compostos, rebalanceamento, independência financeira, armadilhas e golpes |
| **Dívidas** | custo de cada tipo, limites do rotativo e do cheque especial, portabilidade, avalanche e bola de neve, Price e SAC, superendividamento |
| **Reserva de emergência** | quanto guardar conforme o seu trabalho, onde deixar e o que conta como emergência |
| **Orçamento** | 50/30/20, pague-se primeiro, base zero, envelopes, onde cortar, compras por impulso |

Ele traz uma calculadora em Python, sem dependências e sem internet, para não fazer conta de cabeça: juros compostos, metas, quitação de dívidas, Price e SAC, rendimento líquido de renda fixa, equivalência entre LCI e CDB e conversão de taxa mensal para anual.

## Sua pasta

```
minhas-financas/
├── PERFIL.md       quem você é, renda, perfil de risco, degrau atual
├── ORCAMENTO.md    gastos do mês e quanto sobra
├── DIVIDAS.md      cada dívida, juros e plano de quitação
├── RESERVA.md      meta da reserva e onde ela está
├── CARTEIRA.md     seus investimentos e a alocação
├── METAS.md        objetivos com valor, prazo e aporte
├── MERCADO.md      Selic, CDI e IPCA usados nas contas, com data e fonte
└── DIARIO.md       decisões e combinados, com data
```

São arquivos Markdown comuns, no seu computador. Ele avisa antes de anotar e nunca guarda senha, número de cartão, CPF nem dados de conta.

## Instalar

Você precisa do [Claude Code](https://code.claude.com). Para conferir a versão, rode `claude --version`; para atualizar, `claude update`.

### Dentro do Claude Code (recomendado)

1. Abra o Claude Code no terminal, em qualquer pasta.
2. Cole estes comandos, um de cada vez:

   ```
   /plugin marketplace add OtavioFelix-in/money-coach
   /plugin install money-coach@money-coach
   ```

3. Confirme a origem do plugin quando o Claude Code perguntar.
4. Escolha **Install for you** para ter o money-coach em todos os seus projetos.
5. Se aparecer `Run /reload-plugins to apply`, rode `/reload-plugins`.

### Pelo terminal do sistema

Vale também para quem usa o Claude Code no app do desktop ou no VS Code.

```bash
claude plugin marketplace add OtavioFelix-in/money-coach
claude plugin install money-coach@money-coach
```

### Sem plugin

Copie a skill para a sua pasta pessoal. Nesse jeito, você não recebe atualizações.

```bash
git clone https://github.com/OtavioFelix-in/money-coach.git
cp -r money-coach/skills/money-coach ~/.claude/skills/
```
```powershell
git clone https://github.com/OtavioFelix-in/money-coach.git
Copy-Item -Recurse money-coach\skills\money-coach $HOME\.claude\skills\
```

### Atualizar e desinstalar

- **Atualizar sozinho:** rode `/plugin`, aba **Marketplaces**, escolha `money-coach` e selecione **Enable auto-update**.
- **Atualizar agora:** `claude plugin update money-coach@money-coach`
- **Desinstalar:** `claude plugin uninstall money-coach@money-coach` e, para tirar a loja, `claude plugin marketplace remove money-coach`.

## Usar

1. Crie uma pasta, por exemplo `Documentos/minhas-financas`.
2. Abra o Claude Code nela.
3. Chame:

```
/money-coach:money-coach quero organizar minha vida financeira
```

Na primeira vez ele faz a entrevista e monta a pasta. Depois, é só conversar: "posso comprar um celular de R$ 4 mil?", "CDB a 110% ou LCI a 92%?", "como saio do rotativo?", "quanto preciso guardar por mês para dar entrada num apartamento em 3 anos?". Ele também entra sozinho quando o assunto é dinheiro.

## O que ele não faz

- **Não concorda com decisão ruim por insistência.** Muda de opinião com fato novo, não com pressão.
- **Não decide por você.** Mostra a conta e a avaliação dele; a escolha é sua, e ele ajuda a reduzir o estrago se você decidir diferente.
- **Não indica ação, fundo, cripto ou banco específico para comprar**, não prevê preço e não promete retorno. Ensina a escolher.
- **Não inventa taxa.** Selic, CDI e IPCA vêm de fonte oficial, com data, ou ele pergunta.
- **Não guarda dado sensível** e não manda seus dados para lugar nenhum.
- **Não substitui um profissional** certificado em decisões grandes e complexas, como herança, empresa ou patrimônio alto. É uma ferramenta educativa.

## Custo e transparência

- **Parado:** quase nada. Até ser chamado, só a descrição curta dele fica no contexto do Claude.
- **Rodando:** ele lê o núcleo (`SKILL.md`) e só a referência do assunto da conversa (investimentos, dívidas, reserva...), não tudo de uma vez.
- **O núcleo é texto:** arquivos Markdown. A calculadora é um único arquivo Python, sem dependências, que não acessa a internet nem lê arquivos. Nenhum hook, nenhum servidor externo.
- **Regras mudam:** impostos e taxas do Brasil mudam com frequência. Ele confere a regra atual quando ela pesa numa decisão, mas confirme sempre antes de mexer em valores altos.

## Licença

[MIT](LICENSE).

> Projeto independente, sem vínculo com a Anthropic. "Claude" e "Claude Code" são marcas da Anthropic. O mascote e as ilustrações da capa foram feitos para este projeto. Conteúdo educativo: não é recomendação de investimento nem consultoria financeira registrada na CVM.
