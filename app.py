import streamlit as st
import time

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="DevHelper AI", page_icon="🤖")

st.title("🤖 DevHelper AI - Assistente")
st.markdown("---")

# --- BARRA LATERAL ---
with st.sidebar:
    st.header("Configurações")
    modo_uso = st.radio("Escolha a função:", ("Explicar Conceito", "Corrigir Bug", "Sugerir Refatoração"))
    st.info("Modo Simulado Ativado")

# --- FUNÇÃO DE RESPOSTA ---
def resposta_simulada(prompt, categoria):
    time.sleep(1) # Efeito visual
    
    # Validação de Contexto (Regra de Ouro)
    if len(prompt) < 10:
        return "⚠️ Falta Contexto: Por favor, digite uma frase completa ou cole seu código."

    # Respostas Prontas
    if categoria == "Explicar Conceito":
        return "📚 **Explicação:**\n\nUma variável é como uma caixa onde você guarda informações.\nExemplo:\n`nome = 'Tamires'`\nAqui guardamos o texto 'Tamires' dentro da caixa 'nome'."

    elif categoria == "Corrigir Bug":
        return "🐛 **Correção:**\n\nParece um erro de sintaxe.\nVocê provavelmente esqueceu de fechar as aspas.\nVerifique se seu print está assim:\n`print('Texto Aqui')`"

    elif categoria == "Sugerir Refatoração":
        return "✨ **Refatoração:**\n\nPodemos melhorar os nomes das variáveis.\nEm vez de `x` e `y`, use `preco` e `quantidade`.\nIsso deixa o código mais profissional."

    return "Erro interno."

# --- TELA PRINCIPAL ---
st.write("Digite sua dúvida ou cole seu código abaixo:")
entrada_usuario = st.text_area("", height=150)

if st.button("Enviar"):
    if not entrada_usuario:
        st.warning("O campo está vazio.")
    else:
        with st.spinner('Processando...'):
            resposta = resposta_simulada(entrada_usuario, modo_uso)
            st.success("Resposta do Assistente:")
            st.markdown(resposta)