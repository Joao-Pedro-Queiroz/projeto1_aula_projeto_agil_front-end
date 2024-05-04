import streamlit as st
import requests

def fetch_messages(email):
    response = requests.get("https://projeto1-aula-projeto-agil-back-end-x13f.onrender.com", params={'email': email})
    return response.json()['entidades']

def app():
    st.title("Mensagens")
    user_email = st.text_input("Digite o email do usuário")
    if st.button("Buscar Mensagens"):
        messages = fetch_messages(user_email)
        for msg in messages:
            if msg['email_remetente'] == user_email:
                st.markdown(f"**Enviado para {msg['email_destinatário']}**: {msg['mensagem']}")
            else:
                st.markdown(f"**Recebido de {msg['email_remetente']}**: {msg['mensagem']}")

if __name__ == "__main__":
    app()
