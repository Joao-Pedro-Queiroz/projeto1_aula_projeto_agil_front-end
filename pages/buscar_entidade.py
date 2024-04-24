import streamlit as st
import requests

# Configuração da página
st.set_page_config(page_title='Dados da Entidade', page_icon=':bar_chart:', layout='wide')

# Função para obter os dados de um usuário pelo nome
def dados_entidade(nome):
    api_endpoint = ''
    try:
        response = requests.get(url=api_endpoint)
        print('response.status_code:', response.status_code)
        print('response.text:', response.text)
        # Retorna os dados do usuário se a requisição for bem-sucedida
        return response.json() if response.status_code == 200 else None
    except Exception as e:
        print('Erro ao obter os dados do aluno:', e)
        return None
    
# Função para obter os dados do usuário da sessão ou fazer uma nova requisição
def get_session_state(nome):
    if 'user_data' not in st.session_state:
        st.session_state.user_data = dados_entidade(nome)
        # Imprime os dados do usuário para debug
        print('st.session_state.user_data:', st.session_state.user_data)    
    return st.session_state.user_data

def main():
    # Interface do usuário
    st.markdown("# Burscar Entidade")
    st.sidebar.header("Dados da Entidade")

    st.write("## Informe o nome da Entidade:")
    nome = st.text_input("Nome da Entidade")
    print('nome:', nome)
    st.write("##")

    buscar = st.button("Buscar")
    st.write("##")
    if buscar:
        if nome:
            st.sucess("Entidade encontrada!")
            # Obtém os dados do usuário
            user_data = get_session_state(nome)
            print("user_data:", user_data)
            try:
                # Campos de entrada para editar os dados da entidade
                nome = st.text_input("Nome", value=user_data['nome'])
                numero = st.text_input("Número", value=user_data['numero'])
                endereco = st.text_input("Endereço", value=user_data['endereco'])
                cidade = st.text_input("Cidade", value=user_data['cidade'])
                estado = st.text_input("Estado", value=user_data['estado'])
                cep = st.text_input("CEP", value=user_data['cep'])
                cnpj = st.text_input("CNPJ", value=user_data['cnpj'])
                email = st.text_input("Email", value=user_data['email'])
                telefone = st.text_input("Telefone", value=user_data['telefone'])
                site = st.text_input("Site", value=user_data['site'])
                descricao = st.text_input("Descrição", value=user_data['descricao'])
                st.write("##")

                # Botão para salvar os dados do usuário
                salvar = st.button("Salvar")
                if salvar:
                    # atualiza o session state
                    st.session_state.user_data = {
                        "nome": nome,
                        "numero": numero,
                        "endereco": endereco,
                        "cidade": cidade,
                        "estado": estado,
                        "cep": cep,
                        "cnpj": cnpj,
                        "email": email,
                        "telefone": telefone,
                        "site": site,
                        "descricao": descricao
                    }
                    # Atualiza os dados do usuário na API                    
                    # Endpoint da API para editar os dados do aluno
                    api_endpoint = ''
                    data = {}
                    # Montando o payload com os dados do usuário
                    data["Entidade"] = {
                        "nome": nome,
                        "numero": numero,
                        "endereco": endereco,
                        "cidade": cidade,
                        "estado": estado,
                        "cep": cep,
                        "cnpj": cnpj,
                        "email": email,
                        "telefone": telefone,
                        "site": site,
                        "descricao": descricao
                    }
                    try:
                        # Fazendo uma requisição PUT para editar os dados do aluno
                        response = requests.put(url=api_endpoint, json=data)
                        print('response.status_code:', response.status_code)
                        print('response.text:', response.text)
                        # Exibe uma mensagem de sucesso se a edição for bem-sucedida
                        if response.status_code == 200:
                            st.success("Dados da Entidade atualizados com sucesso!")
                        else:
                            st.error("Erro ao atualizar os dados da entidade!")
                    except Exception as e:
                        print('Erro ao editar os dados da entidade:', e)
                        st.error("Erro ao atualizar os dados da entidade!")
            except Exception as e:
                print('Erro ao exibir os dados da entidade:', e)
                st.error("Erro ao exibir os dados da entidade!")

if __name__ == '__main__':
    main()