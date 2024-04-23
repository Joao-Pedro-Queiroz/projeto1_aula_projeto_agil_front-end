import streamlit as st 
import requests

st.set_page_config(page_title="Cadastrar aluno")

def cadastra_aluno(nome, cpf, curso, data_nascimento, entidades, interesses, periodo, projetos):
    api_endpoint = ""
    data = {}

    data["Usuários"] = {
        "nome": nome, 
        "cpf" : cpf,
        "curso" : curso,
        "data_nascimento" : data_nascimento,
        "entidades" : entidades,
        "interesses": interesses,
        "periodo" : periodo,
        "projetos" : projetos
    }
    print(data)

    try:
        response = requests.post(url=api_endpoint, json=data)
        print(response.status_code)
        print(response.json())
    except Exception as e:
        print(e)
    return response, 201 

def main():
    st.markdown("Cadastro de novo aluno")
    st.sidebar.header("Cadastro de novo aluno")

    st.write("## Nome")
    nome = st.text_input("Digite seu nome") 

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
        if nome and cpf and curso and data_nascimento and interesses and periodo:
            response = cadastra_aluno(nome, cpf, curso, data_nascimento, entidades, interesses, periodo, projetos)
            if response.status_code == 201:
                st.success("Aluno cadastrado com sucesso!")
            else:
                st.error("Erro ao cadastrar o aluno")
        else:
            st.error("Todos os campos são obrigatórios exceto entidades e projetos. Por favor preencha-os")

if __name__ == "__main__":
    main()




