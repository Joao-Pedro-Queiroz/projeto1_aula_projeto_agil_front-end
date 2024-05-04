import streamlit as st 
import requests
import yaml

st.set_page_config(page_title="Cadastro de entidade")

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

def cadastra_entidade(nome, data_criacao, apresentacao, area_atuacao, password, presidente, email, vice_presidente, projetos,telefone):
    api_endpoint = "https://projeto1-aula-projeto-agil-back-end-x13f.onrender.com/entidades"
    data = {}

    data = {
        "nome": nome, 
        "data_criacao" : data_criacao,
        "apresentacao" : apresentacao,
        "area_atuacao" : area_atuacao,
        "password" : password,
        "presidente" : presidente,
        "email" : email,
        "vice_presidente" : vice_presidente,
        "projetos" : projetos,
        "info_contato": {
            "email": email,
            "telefone": telefone
        }
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
    st.markdown("Cadastro de nova entidade")
    st.sidebar.header("Cadastro de nova entidade")

    st.write("## Nome")
    nome = st.text_input("Digite o nome da entidade")

    st.write("## Data de Criação")
    data_criacao = st.text_input("Digite a data de criação da entidade")

    st.write("## Apresentação")
    apresentacao = st.text_input("Digite a apresentação da entidade")

    st.write("## Area de Atuação")
    area_atuacao = st.text_input("Digite a area de atuação da entidade")

    st.write("## Senha")
    password = st.text_input("Digite a senha para criação de uma conta")

    st.write("## Presidente")
    presidente = st.text_input("Digite o nome do presidente da entidade")

    st.write("## Email")
    email = st.text_input("Digite o email da entidade")

    st.write("## Telefone")
    telefone = st.text_input("Digite o telefone da entidade")

    st.write("## Vice-Presidente")
    vice_presidente = st.text_input("Digite o nome do vice-presidente da entidade")

    st.write("## Projetos")
    projetos = st.text_input("Digite alguns projetos da entidade")

    st.write("##")
    if st.button("Cadastrar"): 
        if nome and presidente and vice_presidente and email and telefone and area_atuacao and data_criacao and password and projetos and apresentacao:
            response = cadastra_entidade(nome, data_criacao, apresentacao, area_atuacao, password, presidente, email, vice_presidente, projetos,telefone)
            # if response.status_code == 201:
            #     st.write("Entidade cadastrada com sucesso!")
            # else:
            #     st.write("Erro ao cadastrar entidade")
        else:
            st.write("Preencha todos os campos")

        
if __name__ == "__main__":
    main()