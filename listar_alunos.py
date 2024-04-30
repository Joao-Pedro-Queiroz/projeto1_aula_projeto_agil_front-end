import streamlit as st 
import requests
import pandas as pd

st.set_page_config(page_title="Listar alunos")

def listar_alunos():
    api_endpoint = ""
    try:
        response = requests.get(url=api_endpoint)
        if response.status_code == 200:
            return response.json()
        else: 
            st.error("Erro ao listar os alunos")
            return None
    except Exception as e:
        st.error(e)
        return None

def main():
    st.set_page_config(page_title="Alunos")

    st.markdown("#Alunos")

    st.sidebar.header("Alunos")

    dados = listar_alunos()

    if dados:
        st.write("##Tabela com os alunos cadastrados")
        st.write("Aqui estão todos os alunos cadastrados")
        df = pd.DataFrame(dados)
        st.table(df)
    else:
        st.warning("Nenhum aluno cadastrado")

if __name__ == '__main__':
    main()