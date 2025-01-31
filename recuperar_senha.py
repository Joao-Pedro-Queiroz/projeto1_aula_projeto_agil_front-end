import streamlit as st
import requests

def recuperar_senha(email):
    url = f"http://127.0.0.1:5000/senha?email=" + email
    response = requests.get(url)

    if  response.status_code == 200:
        return response.json()["usuario"], response.status_code
    else:
        return {}, response.status_code

def enviar_pedido_de_senha():
    # Valida o e-mail e envia o pedido de recuperação de senha.
    email = st.text_input("Digite seu e-mail para recuperar a senha:")

    if st.button("Enviar"):
        if email:
            usuario, status_code = recuperar_senha(email)
            print(usuario)

            if status_code == 200:
                st.success(f"Sua senha é: {usuario['password']}")
            elif status_code == 404:
                st.error("E-mail não encontrado.")
            elif status_code == 400:
                st.error("Nenhum e-mail fornecido")
            else:
                st.error("Ocorreu um erro ao tentar recuperar a senha.")
        else:
            st.error("Por favor, insira um e-mail válido.")

st.title("Recuperação de Senha")
enviar_pedido_de_senha()
