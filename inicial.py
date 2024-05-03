import streamlit as st
from streamlit_option_menu import option_menu
from pages import page_entidades, contatar_entidade

##HOME

# st.set_page_config(layout="wide")

st.markdown("""
        <style>
            div.st-emotion-cache-79elbk {display: none;}
        </style>
    """, unsafe_allow_html=True)




st.sidebar.image("logo_hub.png", width=250)
st.title("Quero me cadastrar como...")
st.divider()

st.page_link("pages/cadastrar_aluno.py")
st.page_link("pages/cadastrar_entidade.py")



# with st.sidebar:
#     selected = option_menu("",["Home","Alunos", 'Entidades'], icons=None)
#     st.session_state["actual_page"] = selected

# if st.session_state["actual_page"]=="Home":
#     #Header
#     st.title("Bem-vindo ao Hub de Entidades!")

#     st.divider()

# if st.session_state["actual_page"]=="Alunos":
#     #Header
#     st.title("Alunos")
#     st.divider()
#     st.subheader ("Lista de alunos")
   
# if st.session_state["actual_page"]=="Entidades":
#     page_entidades()

# if st.session_state["actual_page"]=="Contatar_Entidade":
#     contatar_entidade()

