import streamlit as st
import requests
import pandas as pd


def cadastra_empresa(data):
    url = "http://127.0.0.1:5000/empresas"
    r = requests.post(url, json=data)
    return r.status_code


st.set_page_config(page_title="Nova Empresa")

st.title(f"Cadastrar nova empresa")

nome = st.text_input("Nome:", placeholder="Digite um nome...")

apresentacao = st.text_input("Apresentação:", placeholder="Digite uma apresentação...")

cargo = st.text_input("Cargo:", placeholder="Digite uma cargo...")

cnpj = st.text_input("CNPJ:", placeholder="Digite um cnpj   ...")

email = st.text_input("Email:", placeholder="Digite um email...")

celular = st.text_input("Celular:", placeholder="Digite um celular...")

linkedin = st.text_input("Linkedin:", placeholder="Digite um linkedin...")

site = st.text_input("Site:", placeholder="Digite um site...")

if st.button("Enviar:"):
    data = {}

    if nome:
        data["nome"] = nome

    if apresentacao:
        data["apresentacao"] = apresentacao

    if cargo:
        data["cargo"] = cargo

    if cnpj:
        data["cnpj"] = cnpj

    if email:
        data["email"] = email

    if celular:
        data["celular"] = celular

    if linkedin:
        data["linkedin"] = linkedin

    if site:
        data["site"] = site

    if len(data) == 8:
        status_code = cadastra_empresa(data)

        if status_code in [200, 201]:
            st.success(f"Bicicleta cadastrado com sucesso")
        else:
            st.error(f"Erro {status_code}. Por favor, tente novamente.")
    else:
        st.error("Por favor, insira todos os dados para cadastrar uma empresa.")