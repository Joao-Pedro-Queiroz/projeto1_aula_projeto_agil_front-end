import streamlit as st
import requests
import pandas as pd


def get_empresa(email):
    url = f"http://127.0.0.1:5000/empresas/{email}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()['empresa'][0]
    elif response.status_code in [400, 404]:
        return {}
    else:
        return None
    

def atualiza_empresa(email, data):
    url = f"http://127.0.0.1:5000/empresas/{email}"
    r = requests.put(url, json=data)
    return r.status_code


def excluir_empresa(email):
    url = f"http://127.0.0.1:5000/empresas/{email}"
    r = requests.delete(url)
    return r.status_code


st.set_page_config(page_title="Dados Bicicleta")

st.title(f"Dados da empresa")
email = st.text_input("Email:", placeholder="Digite um email...")

if st.button("Buscar:"):
    if id:
        st.session_state['empresa'] = get_empresa(email)
    else:
        st.warning("Por favor, insira um email válido.")

if "empresa" in st.session_state and st.session_state['empresa']:
    nome = st.text_input("Marca:", st.session_state['empresa']["nome"])

    apresentacao = st.text_input("Apresentação:", st.session_state['empresa']["apresentacao"])

    cargo = st.text_input("Cargo:", st.session_state['empresa']["cargo"])

    cnpj = st.text_input("CNPJ:", st.session_state['empresa']["cnpj"])

    celular = st.text_input("Celular:", st.session_state['empresa']["celular"])

    linkedin = st.text_input("Linkedin:", st.session_state['empresa']["linkedin"])

    site = st.text_input("Site:", st.session_state['empresa']["site"])

    if st.button("Atualizar dados da empresa"):
        data = {}

        if nome != st.session_state['empresa']["nome"]:
            data["nome"] = nome

        if apresentacao != st.session_state['empresa']["apresentacao"]:
            data["apresentacao"] = apresentacao

        if cargo != st.session_state['empresa']["cargo"]:
            data["cargo"] = cargo

        if cnpj != st.session_state['empresa']["cnpj"]:
            data["cnpj"] = cnpj

        if celular != st.session_state['empresa']["celular"]:
            data["celular"] = celular

        if linkedin != st.session_state['empresa']["linkedin"]:
            data["linkedin"] = linkedin

        if site != st.session_state['empresa']["site"]:
            data["site"] = site

        if len(data) > 0:
            status_code = atualiza_empresa(st.session_state['empresa']["email"], data)

            if status_code == 200:
                del st.session_state['empresa']
                st.success(f"Empresa atualizado com sucesso")
            else:
                st.error(f"Erro {status_code}. Por favor, tente novamente.")
        else:
            st.error("Por favor, altere algum dos dados para atualizar o usuario.")

    if st.button("Excluir empresa"):
        status_code = excluir_empresa(st.session_state['empresa']["email"])

        if status_code == 200:
            del st.session_state['empresa']
            st.success(f"Empresa excluido com sucesso")
        else:
            st.error(f"Erro {status_code}. Por favor, tente novamente.")
            
elif "empresa" in st.session_state and st.session_state['empresa'] == {}:
    st.warning("Email não encontrado ou inválido. Por favor, verifique e tente novamente.")
elif "empresa" in st.session_state and not st.session_state['empresa']:
    st.warning("Erro 500! Por favor, tente novamente mais tarde.")