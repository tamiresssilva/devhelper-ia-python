# Relatório de Uso da IA — Projeto Final

## Onde a IA ajudou
- **Estrutura Rápida:** A IA gerou o esqueleto do aplicativo em Streamlit (interface, botões, barra lateral) em segundos, o que levaria muito mais tempo para fazer do zero.
- **Lógica de Simulação:** Sugeriu a ideia de criar um "Modo Simulado" para que eu pudesse testar o fluxo da aplicação sem gastar créditos de API ou precisar de chaves complexas.
- **Explicação de Erros:** Quando ocorreu o erro de "CommandNotFoundException" no terminal, a IA explicou que era um problema de caminho e sugeriu o comando `python -m streamlit`, que resolveu o problema.

## Onde a IA errou (obrigatório)
- **Erro de Sintaxe no Código Gerado:** Ao pedir para gerar respostas longas, a IA forneceu um código Python usando aspas triplas (`"""`) com indentação incorreta, gerando o erro `SyntaxError: unterminated triple-quoted string literal`.
- **Complexidade Desnecessária:** A IA tentou criar funções complexas de formatação de texto que acabaram quebrando a execução simples do script.

## O que você fez para corrigir/validar
- **Simplificação Manual:** Em vez de tentar debugar as aspas triplas complexas, optei por simplificar o código, usando strings simples e removendo a formatação excessiva que estava causando o erro.
- **Teste Local:** Rodei o comando `python -m streamlit run app.py` repetidamente no meu terminal até garantir que a aplicação abria sem erros no navegador.

## Reflexão final
- **Aprendizado:** Aprendi que não posso confiar cegamente no código que a IA gera ("Copiar e Colar"). O Python é muito rígido com indentação e sintaxe, e a IA muitas vezes ignora isso. A IA funciona melhor como um "copiloto" que dá a ideia inicial, mas eu (o piloto) preciso garantir que o código final seja seguro e executável.