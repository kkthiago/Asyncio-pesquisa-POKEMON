import asyncio
import time
import random
import sys
import os

lista_kanto= ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Pikachu", "Jigglypuff", "Mewtwo", "Mew", "Eevee", "Snorlax", "Arcanine", "Gengar", "Machamp", "Alakazam", "Gyarados"]
lista_johto = ["Chikorita", "Bayleef", "Meganium", "Cyndaquil", "Quilava", "Typhlosion", "Totodile", "Croconaw", "Feraligatr", "Togepi", "Umbreon", "Espeon", "Tyranitar", "Ampharos", "Scizor", "Steelix", "Lugia", "Ho-Oh", "Marill", "Slowking"]
lista_hoenn = ["Treecko", "Grovyle", "Sceptile", "Torchic", "Combusken", "Blaziken", "Mudkip", "Marshtomp", "Swampert", "Gardevoir", "Aggron", "Metagross", "Salamence", "Rayquaza", "Kyogre", "Groudon", "Swellow", "Milotic", "Breloom", "Absol"]
regioes_possiveis = ["Kanto", "Johto", "Hoenn"]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

async def menupokemon():
    print(f"Bem-vindo ao processo de pokemon misterioso!\nVocê receberá 3 pokemons aleatórios da região de (kanto, johto ou hoenn).")
    
async def escolher_pokemon():
    clear_screen()
    total_units = 20
    porcentagem = 0
    tempo_total = random.uniform(3,8)
    unit_tempo = tempo_total / total_units
    unit_tempo_arrumado = round(unit_tempo, 2)
    
    regiao = random.choice(regioes_possiveis)
    if regiao == "Kanto":
        lista = lista_kanto
    elif regiao == "Johto":
        lista = lista_johto
    else:
        lista = lista_hoenn
        
    pokemons = random.sample(lista, 3)
    print(f"Região escolhida: {regiao}.")
    await asyncio.sleep(1)
    
    start = time.perf_counter()
    for i in range(1, total_units + 1):
        bar_preenchida = "█" * i 
        bar_vazia = " " * (total_units - i)
        tempo_passado = i * unit_tempo
        porcentagem += 5
        tempo_restante = tempo_total - tempo_passado
        tempo_restante_formatado = f"{tempo_restante:.2f}s"
        if tempo_restante < 0.01:
            tempo_restante = "CONCLUÍDO"
        linha_completa = f" Progresso: [{bar_preenchida}{bar_vazia}] | Tempo restante: {tempo_restante_formatado} | {porcentagem}%"
        print(linha_completa, end="\r", flush=True)
        await asyncio.sleep(unit_tempo_arrumado)
    clear_screen()
    
    end = time.perf_counter()
    print(f"Trio pokemon escolhido: {pokemons[0]},{pokemons[1]} e {pokemons[2]}")
    print(f"Tempo total de execução: {end - start:.2f} segundos")
    
async def main():
    await menupokemon()
    await asyncio.sleep(5)
    await escolher_pokemon()


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    asyncio.run(main())
