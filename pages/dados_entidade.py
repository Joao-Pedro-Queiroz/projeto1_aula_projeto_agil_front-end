import streamlit as st
import requests

# Configuração da página
st.set_page_config(page_title="Dados da Entidade", page_icon="🧑‍🎓", layout="centered", initial_sidebar_state="expanded")

# Função para obter os dados de uma entidade pelo nome
def get_entidade_details(entidade_nome):
    url = f"http://127.0.0.1:5000/entidades/{entidade_nome}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        error_message = response.json().get('error', 'Erro desconhecido ao buscar a entidade.')
        st.error(error_message)
        return None
    
# Função para atualizar os dados da entidade
def update_entidade(entidade_nome, nome, autor, ano_publicacao, genero):
    url = f"http://127.0.0.1:5000/entidades/{entidade_nome}"
    
    # Definir os campos para editar a entidade
    entidade_data = {
        "titulo": nome,
        "autor": autor,
        "ano_publicacao": ano_publicacao,
        "genero": genero
    }

    response = requests.put(url, json=entidade_data)
    if response.status_code == 200:
        st.success("Entidade atualizada com sucesso!")
    else:
        error_message = response.json().get('error', 'Erro desconhecido ao atualizar a entidade.')
        st.error(error_message)

def delete_entidade(entidade_nome):
    url = f"http://127.0.0.1:5000/entidades/{entidade_nome}"
    response = requests.delete(url)

    if response.status_code == 200:
        st.success("Entidade removida com sucesso!")
    else:
        error_message = response.json().get('error', 'Erro desconhecido ao remover a entidade.')
        st.error(error_message)

def tela_dados_entidades():
    st.title("Dados da Entidade")
    
    with st.form("Formulário Entidade"):
        entidade_nome = st.text_input("Nome da Entidade")
        buscar = st.form_submit_button("Buscar")

        nome = autor = ano_publicacao = genero = ""
        entidade_data = None

        if buscar or 'entidade_data' in st.session_state:
            if buscar:
                entidade_data = get_entidade_details(entidade_nome)
                if entidade_data:
                    st.session_state['entidade_data'] = entidade_data
            else:
                entidade_data = st.session_state['entidade_data']
            
            # Definir os campos para editar a entidade
            nome = st.text_input("Nome", value=entidade_data.get('titulo', ''))
            autor = st.text_input("Autor", value=entidade_data.get('autor', ''))
            ano_publicacao = st.text_input("Ano Publicação", value=entidade_data.get('ano_publicacao', ''))
            genero = st.selectbox("Gênero", ["Romance", "Fantasia", "Ficção Científica"], index=["Romance", "Fantasia", "Ficção Científica"].index(entidade_data.get('genero', "Romance")))

            salvar_alteracoes = st.form_submit_button("Salvar Alterações")
            remover_entidade = st.form_submit_button("Remover Entidade")

            if salvar_alteracoes:
                update_entidade(entidade_nome, nome, autor, ano_publicacao, genero)
                del st.session_state['entidade_data']

            if remover_entidade:
                delete_entidade(entidade_nome)
                del st.session_state['entidade_data']

tela_dados_entidades()
