import streamlit as st 

def contatar_entidade():
    data = st.session_state["entidade"] if "entidade" in st.session_state else st.switch_page("home.py")
    st.title (f'{data["apresentacao"]}')
    st.divider()
    contacts = []
    for key in data["info_contato"].keys():
        contacts.append([key, data["info_contato"][key]])
    st.table(contacts)

contatar_entidade()