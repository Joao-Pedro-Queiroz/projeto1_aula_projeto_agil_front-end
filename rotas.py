import requests

BACK_URL="https://projeto1-aula-projeto-agil-back-end-x13f.onrender.com"

##ENTIDADES 
def get_entidades():
    response = requests.get(f"{BACK_URL}/entidades")
    return response.json()

def get_entidade_by_apresentacao(apresentacao):
    response = requests.get(f"{BACK_URL}/entidades/{apresentacao}")
    return response.json()

def post_entidades(data):
    response = requests.post(f"{BACK_URL}/entidades", data=data)
    return response.json()

##ALUNOS
def get_alunos():
    response = requests.get(f"{BACK_URL}/usuarios")
    return response.json()

def get_aluno_by_apresentacao(nome):
    response = requests.get(f"{BACK_URL}/usuarios/{nome}")
    return response.json()

def post_alunos(data):
    response = requests.post(f"{BACK_URL}/usuarios", data=data)
    return response