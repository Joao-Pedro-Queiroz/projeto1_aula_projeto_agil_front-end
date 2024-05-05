import streamlit as st
from rotas import get_entidades


def page_entidades():
    #Header
    st.title("Entidades")
    st.divider()

    data = get_entidades()["entidades"]
    # Barra de busca
    search_term = st.text_input("Digite o termo de busca:", "")

    st.subheader ("Lista de Entidades")
    # Filtrar os dados com base no termo de busca
    filtered_data = [item for item in data if search_term.lower() in item["apresentacao"].lower()]

    # Exibir resultados
    if filtered_data:
        col1, col2 = st.columns(2)

        with col1:
            for item in filtered_data:
                st.write(item["apresentacao"])
        with col2:
            for item in filtered_data:
                if st.button("Contatar", key=item["apresentacao"]):
                    st.session_state["entidade"] = item
                    st.session_state["actual_page"] = "Contatar_Entidade"
page_entidades()