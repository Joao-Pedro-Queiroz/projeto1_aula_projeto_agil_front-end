import streamlit as st
from rotas import get_usuarios
from rotas import get_alunos


def page_alunos():
    #Header
    st.title("Alunos")
    st.divider()
    data = get_alunos()["usuarios"]
    # Barra de busca
    search_term = st.text_input("Digite o termo de busca:", "")

    st.subheader ("Lista de alunos")
    # Filtrar os dados com base no termo de busca
    filtered_data = [item for item in data if search_term.lower() in item["nome"].lower()]

    # Exibir resultados
    if filtered_data:
        col1, col2 = st.columns(2)
        for item in filtered_data:
            with col1:
                st.write(item['nome'])
            with col2:
                if st.button("Contatar", key=item["nome"]):
                    st.session_state["usuarios"] = item
                    st.session_state["actual_page"] = "Contatar_Aluno"

