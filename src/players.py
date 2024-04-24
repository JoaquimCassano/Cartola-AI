import cartolafc, json

api = cartolafc.Api(attempts=5)

def MinimoParaValorizar():
    data:dict = api._raw_request("https://pb89hpsof3.execute-api.us-east-1.amazonaws.com/prod/escalar/rodadas_anteriores/10").json()
    return data

def RodadaAtual():
    """DOESNT WORK"""
    # return api._raw_request(api._api_url + "/atletas/pontuados/").url
    return 3

def PegarPontuacaoJogadores(rodada_atual:int):
    atletas = {}
    minimos = MinimoParaValorizar()
    for i in range(1, rodada_atual+1):
        data = api.parciais(i)
        for id, atletaObj in data.items():
            if id in atletas.keys():
                atletas[id]['pontos'].append(atletaObj.pontos   )
            else:
                atletas[id] = {
                    'nome': atletaObj.apelido,
                    'pontos': [atletaObj.pontos],
                    'posicao': atletaObj.posicao.id,
                    'mpv': minimos['jogadores'].get(str(id), {}).get('pm', None)
                }
    return atletas

def PegarMedia(pontos:list[int|float]) -> int|float:
    """
    Pega a média das pontuações, porém considera duas vezes a pontuação mais recente
    """
    pontos.append(pontos[-1])
    return sum(pontos) / len(pontos)+1


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
    
