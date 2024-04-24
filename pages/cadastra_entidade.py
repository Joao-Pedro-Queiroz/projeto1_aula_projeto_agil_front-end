import streamlit as st 
import requests

st.set_page_config(page_title="Cadastro de entidade")

def cadastra_entidade(nome, numero, endereco, cidade, estado, cep, cnpj, email, telefone, site, descricao):
    api_endpoint = ""
    data = {}

    data["Entidades"] = {
        "nome": nome, 
        "numero" : numero,
        "endereco" : endereco,
        "cidade" : cidade,
        "estado" : estado,
        "cep" : cep,
        "cnpj" : cnpj,
        "email" : email,
        "telefone" : telefone,
        "site" : site,
        "descricao" : descricao
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
    st.markdown("Cadastro de nova entidade")
    st.sidebar.header("Cadastro de nova entidade")

    st.write("## Nome")
    nome = st.text_input("Digite o nome da entidade")

    st.write("## Número")
    numero = st.text_input("Digite o número da entidade")

    st.write("## Endereço")
    endereco = st.text_input("Digite o endereço da entidade")

    st.write("## Cidade")
    cidade = st.text_input("Digite a cidade da entidade")

    st.write("## Estado") 
    estado = st.text_input("Digite o estado da entidade")

    st.write("## CEP")
    cep = st.text_input("Digite o CEP da entidade")

    st.write("## CNPJ")
    cnpj = st.text_input("Digite o CNPJ da entidade")

    st.write("## Email")
    email = st.text_input("Digite o email da entidade")

    st.write("## Telefone")
    telefone = st.text_input("Digite o telefone da entidade")

    st.write("## Site")
    site = st.text_input("Digite o site da entidade")

    st.write("## Descrição")
    descricao = st.text_input("Digite a descrição da entidade")

    st.write("##")
    if st.button("Cadastrar"): 
        if nome and numero and endereco and cidade and estado and cep and cnpj and email and telefone and site and descricao:
            response = cadastra_entidade(nome, numero, endereco, cidade, estado, cep, cnpj, email, telefone, site, descricao)
            if response.status_code == 201:
                st.write("Entidade cadastrada com sucesso!")
            else:
                st.write("Erro ao cadastrar entidade")
        else:
            st.write("Preencha todos os campos")

        
if __name__ == "__main__":
    main()




