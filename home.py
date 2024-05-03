import streamlit as st
from streamlit_option_menu import option_menu
from pages import page_entidades, contatar_entidade, page_alunos, contatar_aluno

##HOME

st.set_page_config(layout="wide")

st.markdown("""
        <style>
            div.st-emotion-cache-79elbk {display: none;}
        </style>
    """, unsafe_allow_html=True)

st.sidebar.image("logo_hub.png", width=250)
with st.sidebar:
    selected = option_menu("",["Home","Alunos", 'Entidades'], icons=None)
    st.session_state["actual_page"] = selected

if st.session_state["actual_page"]=="Home":
    #Header
    st.title("Bem-vindo ao Hub de Entidades!")
    st.divider()
    st.write("Nosso objetivo é fortalecer a comunicação entre as entidades estudantis e os alunos, garantindo que todos se sintam ouvidos e informados sobre as atividades e decisões que afetam suas experiências educacionais.")
    st.write("Junte-se a nós nesta missão para criar um ambiente acadêmico mais inclusivo e colaborativo. Sua participação é fundamental para o sucesso deste projeto. Vamos trabalhar juntos para construir uma comunidade mais conectada e engajada!")
    st.write("Explore nosso projeto e faça parte da mudança. Juntos, podemos alcançar novos patamares de excelência na comunicação entre entidades e alunos. Vamos começar hoje mesmo!")

##ALUNOS
if st.session_state["actual_page"]=="Alunos":
    #Header
    page_alunos()

if st.session_state["actual_page"]=="Contatar_Aluno":
    contatar_aluno()

##ENTIDADES
if st.session_state["actual_page"]=="Entidades":
    page_entidades()

if st.session_state["actual_page"]=="Contatar_Entidade":
    contatar_entidade()


        