# Usaremos um framework chamado Streamlit, pois ele consegue criar frontend e backend apenas com Python.
# Usaremos a IA da OpenAI.

# Pra rodar um projeto do streamlit, basta usar o comando: streamlit run [nome do arquivo].py

# Nao coloquei uma api_key real, mas para rodar o projeto, basta criar uma conta na OpenAI e pegar a chave de API. Depois, é só substituir a string da api_key pela sua

# Importando bibliotecas
import streamlit as st
from openai import OpenAI

# Criando o modelo da OpenAI, passando a chave de API para autenticação
modelo = OpenAI(api_key="minha_api_key")

# Criando um título para a nossa página web usando Streamlit
st.write("### Chatbot com Streamlit e OpenAI") # Esse hashtag chama-se markdown, e é uma forma de formatar o texto. Quanto mais hashtags, menor o tamanho da fonte.

# Criando uma lista de mensagens se a lista não existir na sessão atual. Se existir, a lista de mensagens é mantida para que o histórico do chat seja preservado.
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# Campo para o usuário digitar a mensagem.
mensagem_usuario = st.chat_input("Digite sua mensagem aqui...")

# Exibindo o histórico de mensagens do chat. Para cada mensagem tem o papel (role) e o conteúdo (content).
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

# Se o usuário digitou a mensagem, ela é exibida na tela, adicionada à lista e enviada para a IA. E a mesma coisa acontece com a resposta da IA.
if mensagem_usuario:
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # É o que envia a mensagem para a IA e define qual versão do modelo será usada.
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )
    resposta_ia = resposta_modelo.choices[0].message.content

    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)