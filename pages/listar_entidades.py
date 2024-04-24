import streamlit as st 
import requests
import pandas as pd

st.set_page_config(page_title="Listar entidades")

def listar_entidades():
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
    st.set_page_config(page_title="Entidades")

    st.markdown("#Entidades")

    st.sidebar.header("Entidades")

    dados = listar_entidades()

    if dados:
        st.write("##Tabela com as entidades cadastradas")
        st.write("Aqui estão todas as entidades cadastradas")
        df = pd.DataFrame(dados)
        st.table(df)
    else:
        st.warning("Nenhuma entidade cadastrada")

if __name__ == '__main__':
    main()