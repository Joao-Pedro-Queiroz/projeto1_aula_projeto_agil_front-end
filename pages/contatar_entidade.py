import streamlit as st 
import requests


def contatar_entidade():
    data = st.session_state.get("entidades")

    if not data:
        st.error("Nenhuma entidade selecionado.")
        return
    
    st.title(data["nome"])
    st.divider()
    
    email_destinatário = st.text_input("Email destinatário:", data['email'])
    email_remetente = st.text_input("Email remetente:")
    assunto = st.text_input("Digite o assunto do email")
    mensagem = st.text_area("Digite a mensagem do email")

    if st.button("Enviar mensagem"):
        url = "https://projeto1-aula-projeto-agil-back-end-x13f.onrender.com/mensagens"
        payload = {
            "email_destinatário": email_destinatário,
            "email_remetente": email_remetente,
            "assunto": assunto,
            "mensagem": mensagem
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            st.success("Mensagem enviada com sucesso.")
        else:
            st.error("Erro ao enviar mensagem.")
        

contatar_entidade()