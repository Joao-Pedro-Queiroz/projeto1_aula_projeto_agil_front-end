import streamlit as st 


def contatar_aluno():
    data = st.session_state.get("usuarios")

    if not data:
        st.error("Nenhum aluno selecionado.")
        return
    
    st.title(data["nome"])
    st.divider()
    
    email_destinatário = st.text_input("Email destinatário:", data['email'])
    email_remetente = st.text_input("Email remetente:")
    assunto = st.text_input("Digite o assunto do email")
    mensagem = st.text_area("Digite a mensagem do email")

    if st.button("Enviar menagem"):
        

contatar_aluno()