import streamlit as st 
import requests
import yaml

st.set_page_config(page_title="Cadastrar aluno")

st.markdown("""
        <style>
            div.st-emotion-cache-79elbk {display: none;}
        </style>
    """, unsafe_allow_html=True)

st.sidebar.image("logo_hub.png", width=250)

def save_on_yml(data):
    config = {}
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    config["credentials"]["usernames"][data["nome"]] = {
        "email": data["email"],
        "name": data["nome"],
        "password": data["password"],
    }
    
    with open("config.yaml", "w") as file:
        yaml.dump(config, file, default_flow_style=False)


def cadastra_aluno(nome, cpf,email, curso, data_nascimento, entidades, interesses, periodo, password, projetos):
    api_endpoint = "https://projeto1-aula-projeto-agil-back-end-x13f.onrender.com/usuarios"
    data = {}

    data = {
        "nome": nome, 
        "cpf" : cpf,
        "email" : email,
        "curso" : curso,
        "data_nascimento" : data_nascimento,
        "entidades" : entidades,
        "interesses": interesses,
        "periodo" : periodo,
        "password" : password,
        "projetos" : projetos,

    }
    print(data)

    try:
        response = requests.post(url=api_endpoint, json=data)
        
        save_on_yml(data)
        
        if response.status_code == 201:
            st.switch_page("login.py")
    except Exception as e:
        print(e)
    return response, 201 

def main():
    st.markdown("Cadastro de novo aluno")
    st.sidebar.header("Cadastro de novo aluno")

    st.write("## Nome")
    nome = st.text_input("Digite seu nome") 

    st.write("## E-mail")
    email = st.text_input("Digite seu e-mail") 

    st.write("## Senha")
    password = st.text_input("Digite sua senha") 

    st.write("## CPF")
    cpf = st.text_input("Digite seu CPF")

    st.write("## Curso")
    curso = st.text_input("Digite seu curso")

    st.write("## Data de Nascimento")
    data_nascimento = st.text_input("Digite sua data de nascimento") 

    st.write("## Entidades")
    entidades = st.text_input("Digite as entidades que você participa (caso participe de nenhuma, deixe vazio)")

    st.write("## Interesses")
    interesses = st.text_input("Digite seus interesses")

    st.write("## Período")
    periodo = st.text_input("Digite seu período")

    st.write("## Projetos")
    projetos = st.text_input("Quais projetos você participa? (Se participa de nenhum, deixe em branco)")

    st.write("##")
    if st.button("Cadastrar"): 
        if nome and email and password and cpf and curso and data_nascimento and interesses and periodo:
                cadastra_aluno(nome, cpf,email, curso, data_nascimento, entidades, interesses, periodo,password, projetos)
                st.success("Aluno cadastrado com sucesso.")
        else:
            st.error("Todos os campos são obrigatórios exceto entidades e projetos. Por favor preencha-os")

if __name__ == "__main__":
    main()