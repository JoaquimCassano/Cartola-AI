import players
from constants import *

def SelectBestPlayers(position:Posicoes, quantidade:int) -> list: # type: ignore
    atletas = players.PegarPontuacaoJogadores(players.RodadaAtual())
    for id, atleta in atletas.items():
        if atleta['posicao'] == position:
            atleta['media'] = players.PegarMedia(atleta['pontos'])
        else:
            atletas.pop(id)
    
