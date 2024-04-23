import streamlit as st
import requests
import pandas as pd


st.set_page_config(page_title="Lista Empresas")

url = "http://127.0.0.1:5000/empresas"

r = requests.get(url)
status_code_resposta = r.status_code

if status_code_resposta == 200:
    empresas = r.json()["empresas"]

    st.title("Empresas cadastrados/Minhas empresas")

    df = pd.DataFrame(empresas)

    st.table(df)
elif status_code_resposta == 404:
    st.title(f"Erro 404")
    st.write("API não encontrado! Por favor, tente novamente")
elif status_code_resposta == 500:
    st.title(f"Erro 500")
    st.write("A API está com problema! Por favor, tente novamente mais tarde")
else:
    st.title(f"Erro {status_code_resposta}")
    st.write("Por favor, tente novamente")