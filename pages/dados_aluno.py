import streamlit as st
import requests

# Configuração da página
st.set_page_config(page_title='Dados do Aluno', page_icon=':bar_chart:', layout='wide')

# Função para obter os dados de um usuário pelo nome
def dados_aluno(nome):
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
        st.session_state.user_data = dados_aluno(nome)
        # Imprime os dados do usuário para debug
        print('st.session_state.user_data:', st.session_state.user_data)    
    return st.session_state.user_data

def main():
    # Interface do usuário
    st.markdown("# Burscar Aluno")
    st.sidebar.header("Dados do Aluno")

    st.write("## Informe o nome do aluno:")
    nome = st.text_input("Nome do aluno")
    print('nome:', nome)
    st.write("##")

    buscar = st.button("Buscar")
    st.write("##")
    if buscar:
        if nome:
            st.sucess("Usuário encontrado!")
            # Obtém os dados do usuário
            user_data = get_session_state(nome)
            print("user_data:", user_data)
            try:
                # Campos de entrada para editar os dados do usuário
                nome = st.text_input("Nome", value=user_data['nome'])
                cpf = st.text_input("CPF", value=user_data['cpf'])
                data_nascimento = st.text_input("Data de Nascimento", value=user_data['data_nascimento'])
                entidades = st.text_input("Entidades", value=user_data['entidades'])
                interesses = st.text_input("Interesses", value=user_data['interesses'])
                periodo = st.text_input("Período", value=user_data['periodo'])
                projetos = st.text_input("Projetos", value=user_data['projetos'])
                st.write("##")

                # Botão para salvar os dados do usuário
                salvar = st.button("Salvar")
                if salvar:
                    # atualiza o session state
                    st.session_state.user_data = {
                        "nome": nome,
                        "cpf": cpf,
                        "data_nascimento": data_nascimento,
                        "entidades": entidades,
                        "interesses": interesses,
                        "periodo": periodo,
                        "projetos": projetos
                    }
                    # Atualiza os dados do usuário na API                    
                    # Endpoint da API para editar os dados do aluno
                    api_endpoint = ''
                    data = {}
                    # Montando o payload com os dados do usuário
                    data["Usuario"] = {
                        "nome": nome,
                        "cpf": cpf,
                        "data_nascimento": data_nascimento,
                        "entidades": entidades,
                        "interesses": interesses,
                        "periodo": periodo,
                        "projetos": projetos
                    }
                    try:
                        # Fazendo uma requisição PUT para editar os dados do aluno
                        response = requests.put(url=api_endpoint, json=data)
                        print('response.status_code:', response.status_code)
                        print('response.text:', response.text)
                        # Exibe uma mensagem de sucesso se a edição for bem-sucedida
                        if response.status_code == 200:
                            st.success("Dados do aluno atualizados com sucesso!")
                        else:
                            st.error("Erro ao atualizar os dados do aluno!")
                    except Exception as e:
                        print('Erro ao editar os dados do aluno:', e)
                        st.error("Erro ao atualizar os dados do aluno!")
            except Exception as e:
                print('Erro ao exibir os dados do aluno:', e)
                st.error("Erro ao exibir os dados do aluno!")

if __name__ == '__main__':
    main()