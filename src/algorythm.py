import players
from constants import *
import rich

def SelectBestPlayers(position:any, quantidade:int) -> list: # type: ignore
    atletas = players.PegarPontuacaoJogadores(players.RodadaAtual())
    playersOutOfPosition = [id for id, atleta in atletas.items() if atleta['posicao'] != position or atleta['status'] != Status.PROVAVEL]
    for id in playersOutOfPosition:
        atletas.pop(id)
    
    return sorted(atletas.items(), key=lambda x: x[1]['media']-x[1]['mpv'], reverse=True)[:quantidade]
    
if __name__ == "__main__":
    rich.print(f"[bold red]TIME DO ALGORITMO[/bold red]")
    rich.print(f"[bold blue]GOLEIRO:[/bold blue]: {SelectBestPlayers(Posicoes.GOLEIRO, 1)[0]}") #type: ignore
    zagueiros = SelectBestPlayers(Posicoes.ZAGUEIRO, 2)
    rich.print(f"[bold green]ZAGUEIRO:[/bold green]: {zagueiros[0]}") #type: ignore
    rich.print(f"[bold green]ZAGUEIRO:[/bold green]: {zagueiros[1]}") #type: ignore
    lat = SelectBestPlayers(Posicoes.LATERAL, 2)
    rich.print(f"[bold green]LATERAL:[/bold green]: {lat[0]}") #type: ignore
    rich.print(f"[bold green]LATERAL:[/bold green]: {lat[1]}") #type: ignore
    meias = SelectBestPlayers(Posicoes.MEIA, 4)
    rich.print(f"[bold yellow]MEIAS:[/bold yellow]: {meias[0]}") #type: ignore
    rich.print(f"[bold yellow]MEIAS:[/bold yellow]: {meias[1]}") #type: ignore
    rich.print(f"[bold yellow]MEIAS:[/bold yellow]: {meias[2]}") #type: ignore
    rich.print(f"[bold yellow]MEIAS:[/bold yellow]: {meias[3]}") #type: ignore
    ata = SelectBestPlayers(Posicoes.ATACANTE, 2)
    rich.print(f"[bold red]ATACANTES:[/bold red]: {ata[0]}") #type: ignore
    rich.print(f"[bold red]ATACANTES:[/bold red]: {ata[1]}") #type: ignore
