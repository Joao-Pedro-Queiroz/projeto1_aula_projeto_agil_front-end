import streamlit as st
import requests
import pandas as pd
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

#Página de login

##HOME
with st.sidebar:
    st.sidebar.image("logo_hub.png", width=250)
    selected = option_menu("",["Home","Alunos", 'Entidades','Empresas'], icons=None)
    # st.sidebar.image("imagem_na_aba.png", width=300)

if selected=="Home":
    #Header
    st.title("Bem-vindo ao Hub de Entidades!")

    st.divider()

if selected=="Alunos":
    #Header
    st.title("Alunos")
    st.divider()
    st.subheader ("Lista de alunos")

if selected=="Entidades":
    #Header
    st.title("Entidades")
    st.divider()

    # Dados de exemplo
    data = ["Maçã", "Banana", "Cereja", "Laranja", "Pêssego", "Abacaxi", "Uva"]

        # Barra de busca
    search_term = st.text_input("Digite o termo de busca:", "")

    st.subheader ("Lista de Entidades")
    # Filtrar os dados com base no termo de busca
    filtered_data = [item for item in data if search_term.lower() in item.lower()]

    # Exibir resultados
    if filtered_data:
        for item in filtered_data:
            st.write(item)
        # Adicionar botão "Contatar" ao lado do nome da entidade
        if st.button("Contatar", key=item):
            # Ação ao clicar no botão (pode ser redirecionamento para outra página)
            st.write("Contatou:", item)
else:
    st.write("Nenhum resultado encontrado.")
        