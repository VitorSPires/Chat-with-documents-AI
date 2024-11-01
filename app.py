from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from bucarVetores import *
import streamlit as st
import time

# carrega todas as variáveis de ambientes
load_dotenv()

# selecionando o modelo escolhido
llm = GoogleGenerativeAI(model="gemini-1.5-flash-latest")

#Página web para melhor visualização
st.set_page_config(page_title='Assistente Unih')
st.header('Assistente Unih')

st.markdown(
    r"""
    <style>
    .stAppToolbar  {
        visibility: hidden;
    }
    
    div[data-testid="InputInstructions"] > span:nth-child(1) {
        visibility: hidden;
    }

    [data-testid="stDecoration"] {background: linear-gradient(90deg, rgba(0,148,124,1) 0%, rgba(1,66,132,1) 100%);}
    </style>
    """, unsafe_allow_html=True
)

col1, col2 = st.columns([4,1]) 

instr = ''
with col1:
    prompt = st.text_input(
        instr,
        value=instr,
        placeholder="Digite a sua dúvida aqui...",
        label_visibility='collapsed'
    )
with col2:
    submitted = st.button('Enviar')

if prompt and submitted:
    with st.spinner('Carregando...'):
        newPrompt = llm.invoke(f'Use o texto a seguir para gerar uma frase com a ideia principal desse tema, que será utilizada para encontrar trechos de documentação numa busca vetorial. A frase deve estar em espanhol. Não dê instruções nem diga o que está fazendo.\n{prompt}')
        result = buscar_texto_similar(newPrompt)
        #st.write(f'Texto original: {prompt}')
        #st.write(f'Busca vetorial feita a partir de: {newPrompt}\n')
        #t.write(f'{result}')
        st.write(f"{llm.invoke(f'Você é um agente da equipe de suporte, e receberá trechos de uma documentação que deve usar para responder a seguinte pergunta em português: {prompt}. {result}')}")
