# 🤖 DevHelper AI — Assistente de Programação

Este projeto é um **Assistente de Programação Inteligente** desenvolvido em Python. O objetivo é ajudar desenvolvedores iniciantes a entenderem conceitos, corrigirem bugs e melhorarem a qualidade de seu código, utilizando Inteligência Artificial de forma responsável.

> **Projeto Final:** Demonstração de uso de IA como ferramenta de produtividade.

---

## 🚀 Funcionalidades

O assistente possui três modos principais de operação:

1.  **📚 Explicar Conceito:** Traduz termos técnicos (ex: Loops, Variáveis, Arrays) para uma linguagem simples e didática.
2.  **🐛 Corrigir Bug:** Analisa erros de sintaxe ou lógica e sugere correções diretas.
3.  **✨ Sugerir Refatoração:** Propõe melhorias no código para torná-lo mais limpo ("Clean Code") e profissional.

### 🛡️ A "Regra de Ouro"
O diferencial deste projeto é a responsabilidade na resposta. Se o usuário fornecer um prompt vago ou sem contexto (ex: apenas "erro"), o assistente **não tenta adivinhar**. Ele solicita mais informações (linguagem, código completo, mensagem de erro) antes de responder.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Interface:** Streamlit (Framework Web para Data Apps)
* **Lógica:** Processamento de Texto Simulado (Mock) para validação de conceitos.

---

## 📦 Como Executar o Projeto

Pré-requisitos: Você precisa ter o [Python](https://www.python.org/) instalado.

### 1. Instalação das dependências
Abra o terminal na pasta do projeto e instale o Streamlit:

```bash
pip install streamlit