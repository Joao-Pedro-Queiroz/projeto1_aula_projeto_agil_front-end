import streamlit as st 
from streamlit_authenticator import Authenticate
import yaml
from yaml.loader import SafeLoader

st.markdown("""
        <style>
            div.st-emotion-cache-79elbk {display: none;}
        </style>
    """, unsafe_allow_html=True)
st.sidebar.image("logo_hub.png", width=250)


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('main',fields={'Form name':'Login', 'Username':'Username', 'password':'Password', 'Login':'Login'})

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    
    st.session_state["actual_page"] = "Home"
    st.switch_page('pages/home.py')
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')


st.divider()
st.write("Eu quero me cadastrar como...")

st.page_link("pages/cadastrar_aluno.py")
st.page_link("pages/cadastrar_entidade.py")

