import requests
import json
from config import conf

lista_estacoes = {}
lista_destinos = {}
api = 'https://api.metrolisboa.pt:8243/estadoServicoML/1.0.1/'
auth = conf["key"]

def atribuirAbrevNome():
    r = requests.get('{}infoEstacao/todos'.format(api), headers = {"Authorization": auth})
    response = json.loads(r.text)

    for res in response['resposta']:
        lista_estacoes.update({res['stop_id']: res['stop_name']})

def atribuirIDDestinoNome():
    r = requests.get('{}infoDestinos/todos'.format(api), headers = {"Authorization": auth})
    response = json.loads(r.text)

    for res in response['resposta']:
        lista_destinos.update({res['id_destino']: res['nome_destino']})

def getNomeDestino(abrev):
    return lista_destinos[abrev]

def getNomeEstacao(abrev):
    return lista_estacoes[abrev]

def getInfoEstacao(estacao):
    r = requests.get('{}infoEstacao/{}'.format(api, estacao), headers = {"Authorization": auth})
    response = json.loads(r.text)

    for res in response['resposta']:
        print("Nome da estação: ", res['stop_name'])
        print("Linha: ", res['linha'])
        print("ID da zona: ", res['zone_id'])

def getTemposLinha(nomeLinha):
    r = requests.get('{}tempoEspera/Linha/{}'.format(api, nomeLinha), headers = {"Authorization": auth})
    response = json.loads(r.text)

    for res in response['resposta']:
        print("LINHA {} -> Faltam {} segundos para a chegada do comboio {} com destino a {} à estação {}".format(nomeLinha.upper(), res['tempoChegada1'], res['comboio'], getNomeDestino(res['destino']) , getNomeEstacao(res['stop_id'])))




atribuirAbrevNome()
atribuirIDDestinoNome()

getTemposLinha("Amarela")

#getInfoEstacao("AX")