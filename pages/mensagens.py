import streamlit as st
import requests

def fetch_messages():
    response = requests.get("https://projeto1-aula-projeto-agil-back-end-x13f.onrender.com/mensagens")
    return response.json()['mensagens']

def app():
    st.title("Mensagens")
    user_email = st.text_input("Digite o email do usuário")
    if st.button("Buscar Mensagens"):
        messages = fetch_messages()
        for msg in messages:
            if msg['email_remetente'] == user_email:
                st.markdown(f"**Enviado para {msg['email_destinatário']}**:")
                st.markdown(f":yellow[Assunto: {msg['assunto']}]")
                st.markdown(f":yellow[Mensagem: {msg['mensagem']}]")
                st.divider()
            elif msg['email_destinatário'] == user_email:
                st.markdown(f"**Recebido de {msg['email_remetente']}**:")
                st.markdown(f":yellow[Assunto: {msg['assunto']}]")
                st.markdown(f":yellow[Mensagem: {msg['mensagem']}]")
                st.divider()

if __name__ == "__main__":
    app()
