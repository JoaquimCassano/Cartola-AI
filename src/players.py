import cartolafc, json

api = cartolafc.Api(attempts=5)

def MinimoParaValorizar():
    data:dict = api._raw_request("https://pb89hpsof3.execute-api.us-east-1.amazonaws.com/prod/escalar/rodadas_anteriores/10").json()
    return data

def RodadaAtual():
    """
    Retorna o número da rodada atual
    """
    data =  api._raw_request(api._api_url + "/atletas/mercado/").json()['atletas'][0]['rodada_id']
    return data

def PegarPontuacaoJogadores(rodada_atual:int):
    atletas = {}
    minimos = MinimoParaValorizar()
    mercadoPlayers = api.mercado_atletas()

    for i in range(1, rodada_atual+1):
        data = api.parciais(i)
        for id, atletaObj in data.items():
            if id in atletas.keys():
                atletas[id]['pontos'].append(atletaObj.pontos)
                atletas[id]['media']= PegarMedia(atletas[id]['pontos'])
            else:
                atletas[id] = {
                    'nome': atletaObj.apelido,
                    'pontos': [atletaObj.pontos],
                    'media': PegarMedia([atletaObj.pontos]),
                    'posicao': atletaObj.posicao.id,
                    'mpv': minimos['jogadores'].get(str(id), {}).get('pm', None),
                }

    # pegar status
    for player in mercadoPlayers:
        if player.id in atletas.keys():
            atletas[player.id]['status'] = player.status.id if player.status else None
    return atletas

def PegarMedia(pontos:list[int|float]) -> int|float:
    """
    Pega a média das pontuações
    """
    return sum(pontos) / len(pontos)


if __name__ == "__main__":
        res = PegarPontuacaoJogadores(3)
        try:
                import rich
                rich.print_json(data=res)
                with open("players.json", "w") as f:
                    f.write(json.dumps(res))
        except:
                print(res)
                with open("players.json", "w") as f:
                    f.write(json.dumps(res))
        
        print(RodadaAtual())