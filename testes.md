# Testes do Assistente

Realizei os testes abaixo executando a aplicação localmente (`python -m streamlit run app.py`) no modo simulado para validar a lógica de resposta e a regra de contexto.

## Teste 1 — Explicação
**Pergunta:**
"Poderia explicar o que é uma variável em Python?"

**Resposta do Assistente:**
📚 **Explicação:**
Uma variável é como uma caixa onde você guarda informações.
Exemplo:
`nome = 'Tamires'`
Aqui guardamos o texto 'Tamires' dentro da caixa 'nome'.

**Observação:**
A resposta foi didática e adequada para iniciantes. O uso da analogia da "caixa" facilita muito o entendimento de quem nunca programou.

---

## Teste 2 — Bug
**Pergunta:**
"Estou com erro no meu código print ola mundo"

**Código Inserido:**
`print("Ola Mundo`

**Resposta do Assistente:**
🐛 **Correção:**
Parece um erro de sintaxe.
Você provavelmente esqueceu de fechar as aspas.
Verifique se seu print está assim:
`print('Texto Aqui')`

**Observação:**
O assistente foi direto ao ponto. Identificou que faltavam aspas (SyntaxError), que é um dos erros mais comuns, e já deu a solução pronta.

---

## Teste 3 — Refatoração
**Pergunta:**
"Como posso melhorar este código simples?"

**Código Inserido:**
`x = 10`
`y = 20`

**Resposta do Assistente:**
✨ **Refatoração:**
Podemos melhorar os nomes das variáveis.
Em vez de `x` e `y`, use `preco` e `quantidade`.
Isso deixa o código mais profissional.

**Observação:**
A sugestão foi excelente porque focou em "Clean Code" (código limpo). Para um iniciante, aprender a dar nomes significativos é mais importante do que aprender atalhos complexos.

---

## Teste Extra — Regra de Ouro (Contexto)
**Pergunta:**
"Erro"

**Resposta do Assistente:**
⚠️ Falta Contexto: Por favor, digite uma frase completa ou cole seu código.

**Observação:**
O sistema barrou a pergunta vaga, cumprindo o requisito de não "chutar" respostas sem ter informações suficientes.



# Testes do Assistente

Testes realizados localmente utilizando o "Modo Simulado" do DevHelper AI.

## Teste 1 — Explicação
**Pergunta:** Explicar Conceito: "O que é variável?"
**Resposta:** "📚 **Explicação:**
Uma variável é como uma caixa onde você guarda informações.
Exemplo:
`nome = 'Tamires'`
Aqui guardamos o texto 'Tamires' dentro da caixa 'nome'."
**Observação:** A resposta foi muito didática. A analogia da "caixa" é excelente para quem está começando, pois torna um conceito abstrato em algo concreto.

## Teste 2 — Bug
**Pergunta:** Corrigir Bug: "Meu print deu erro"
**Código:** `print("Ola mundo`
**Erro (se houver):** SyntaxError (simulado)
**Resposta:** "🐛 **Correção:**
Parece um erro de sintaxe.
Você provavelmente esqueceu de fechar as aspas.
Verifique se seu print está assim:
`print('Texto Aqui')`"
**Observação:** O assistente identificou corretamente o erro mais comum de iniciantes (esquecer aspas) e forneceu a solução direta sem usar termos técnicos complicados.

## Teste 3 — Refatoração
**Pergunta:** Sugerir Refatoração: "Melhore esse código"
**Código:** `x = 10`, `y = 20`
**Resposta:** "✨ **Refatoração:**
Podemos melhorar os nomes das variáveis.
Em vez de `x` e `y`, use `preco` e `quantidade`.
Isso deixa o código mais profissional."
**Observação:** A sugestão foca em "Clean Code" (código limpo). É uma dica valiosa para iniciantes, pois ensina que o código deve ser legível por humanos, não apenas por máquinas.