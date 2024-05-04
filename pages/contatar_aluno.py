import streamlit as st 
import smtplib

st.set_page_config(page_title="Contatar aluno")
def contatar_aluno():
    data = st.session_state.get("usuarios")
    if not data:
        st.error("Nenhum aluno selecionado.")
        return
    
    st.title(data["nome"])
    st.divider()
    
    st.write(f"Email: {data['email']}")

contatar_aluno()

def send_email(sender, to_email, subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("SEU_EMAIL", "SUA_SENHA")
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail("SEU_EMAIL", to_email, email_message)
        server.close()
        return "Email enviado com sucesso!"
    except Exception as e:
        return str(e)

def app():
    st.title("Enviar email")
    sender = st.text_input("Digite seu email")
    to_email = st.text_input("Digite o email do destinatário")
    subject = st.text_input("Digite o assunto do email")
    message = st.text_area("Digite a mensagem do email")
    if st.button("Enviar Email"):
        response = send_email(sender, to_email, subject, message)
        st.success(response)

if __name__ == "__main__":
    app()