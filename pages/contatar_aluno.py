import streamlit as st 
def contatar_aluno():
    data = st.session_state.get("usuarios")
    if not data:
        st.error("Nenhum aluno selecionado.")
        return
    
    st.title(data["nome"])
    st.divider()
    
    st.write(f"Email: {data['email']}")
