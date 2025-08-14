import asyncio
import time
import random
import sys
import os

lista_kanto = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Pikachu","Jigglypuff","Mewtwo","Mew","Eevee","Snorlax","Arcanine","Gengar","Machamp","Alakazam","Gyarados"]
lista_johto = ["Chikorita","Bayleef","Meganium","Cyndaquil","Quilava","Typhlosion","Totodile","Croconaw","Feraligatr","Togepi","Umbreon","Espeon","Tyranitar","Ampharos","Scizor","Steelix","Lugia","Ho-Oh","Marill","Slowking"]
lista_hoenn  = ["Treecko","Grovyle","Sceptile","Torchic","Combusken","Blaziken","Mudkip","Marshtomp","Swampert","Gardevoir","Aggron","Metagross","Salamence","Rayquaza","Kyogre","Groudon","Swellow","Milotic","Breloom","Absol"]

regioes_possiveis = ["Kanto", "Johto", "Hoenn"]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# lock para que os writes ANSI+linha sejam atômicos
print_lock = None  # será inicializado em main()

async def menupokemon():
    print("Bem-vindo ao processo de pokemon misterioso!")
    print("Você receberá 3 pokemons aleatórios das regiões Kanto, Johto e Hoenn.\n")
    await asyncio.sleep(0.8)

# função auxiliar para atualizar linha específica (index 0..2)
def write_line_for_index(index: int, label: str, texto: str):
    """
    Usa códigos ANSI para mover o cursor para a linha correta,
    limpar a linha e escrever o texto (sem criar linhas extras).
    index=0 => primeira linha do bloco (Kanto), index=1 => segunda (Johto), ...
    """
    # número de linhas do bloco (Kanto, Johto, Hoenn)
    block_lines = len(regioes_possiveis)
    # mover cursor para cima (block_lines - index) linhas para chegar na linha alvo
    up = block_lines - index
    # sequências:
    # 1) move up N
    # 2) clear entire line (\x1b[2K)
    # 3) carriage return e escreve "Label texto"
    # 4) move cursor de volta para onde estava (move down N)
    seq = ""
    seq += f"\x1b[{up}A"      # move cursor up para linha alvo
    seq += "\x1b[2K"         # limpa a linha
    seq += f"\r{label} {texto}"  # escreve sem \n
    seq += f"\x1b[{up}B"     # retorna para posição original
    sys.stdout.write(seq)
    sys.stdout.flush()

async def escolher_pokemon_kanto(index: int):
    global print_lock
    total_units = 20
    tempo_total = random.uniform(1, 5)
    unit_tempo = tempo_total / total_units

    lista = lista_kanto
    regiao = "Kanto"
    # random.choice já devolve string
    pokemon_kanto = random.choice(lista)

    # escreve o cabeçalho inicial da linha (sem bloquear muito)
    async with print_lock:
        write_line_for_index(index, f"{regiao}:", "Iniciando...")
    await asyncio.sleep(0.8)

    porcentagem = 0
    for i in range(1, total_units + 1):
        bar_preenchida = "█" * i
        bar_vazia = " " * (total_units - i)
        tempo_passado = i * unit_tempo
        porcentagem = int(i * 100 / total_units)
        tempo_restante = max(0.0, tempo_total - tempo_passado)
        tempo_restante_formatado = f"{tempo_restante:.2f}s" if tempo_restante > 0.0 else "CONCLUÍDO"
        linha_completa = f"Progresso: [{bar_preenchida}{bar_vazia}] | Tempo restante: {tempo_restante_formatado} | {porcentagem}%"
        async with print_lock:
            write_line_for_index(index, f"{regiao}:", linha_completa)
        # aguarda a fração de tempo (assíncrono)
        await asyncio.sleep(unit_tempo)

    # final
    async with print_lock:
        write_line_for_index(index, f"{regiao}:", f"Concluído: {pokemon_kanto}")
    await asyncio.sleep(0.2)
    return pokemon_kanto

async def escolher_pokemon_johto(index: int):
    global print_lock
    total_units = 20
    tempo_total = random.uniform(1, 5)
    unit_tempo = tempo_total / total_units

    lista = lista_johto
    regiao = "Johto"
    pokemon_johto = random.choice(lista)

    async with print_lock:
        write_line_for_index(index, f"{regiao}:", "Iniciando...")
    await asyncio.sleep(0.8)

    porcentagem = 0
    for i in range(1, total_units + 1):
        bar_preenchida = "█" * i
        bar_vazia = " " * (total_units - i)
        porcentagem = int(i * 100 / total_units)
        tempo_passado = i * unit_tempo
        tempo_restante = max(0.0, tempo_total - tempo_passado)
        tempo_restante_formatado = f"{tempo_restante:.2f}s" if tempo_restante > 0.0 else "CONCLUÍDO"
        linha_completa = f"Progresso: [{bar_preenchida}{bar_vazia}] | Tempo restante: {tempo_restante_formatado} | {porcentagem}%"
        async with print_lock:
            write_line_for_index(index, f"{regiao}:", linha_completa)
        await asyncio.sleep(unit_tempo)

    async with print_lock:
        write_line_for_index(index, f"{regiao}:", f"Concluído: {pokemon_johto}")
    await asyncio.sleep(0.2)
    return pokemon_johto

async def escolher_pokemon_hoenn(index: int):
    global print_lock
    total_units = 20
    tempo_total = random.uniform(1, 5)
    unit_tempo = tempo_total / total_units

    lista = lista_hoenn
    regiao = "Hoenn"
    pokemon_hoenn = random.choice(lista)

    async with print_lock:
        write_line_for_index(index, f"{regiao}:", "Iniciando...")
    await asyncio.sleep(0.8)

    porcentagem = 0
    for i in range(1, total_units + 1):
        bar_preenchida = "█" * i
        bar_vazia = " " * (total_units - i)
        porcentagem = int(i * 100 / total_units)
        tempo_passado = i * unit_tempo
        tempo_restante = max(0.0, tempo_total - tempo_passado)
        tempo_restante_formatado = f"{tempo_restante:.2f}s" if tempo_restante > 0.0 else "CONCLUÍDO"
        linha_completa = f"Progresso: [{bar_preenchida}{bar_vazia}] | Tempo restante: {tempo_restante_formatado} | {porcentagem}%"
        async with print_lock:
            write_line_for_index(index, f"{regiao}:", linha_completa)
        await asyncio.sleep(unit_tempo)

    async with print_lock:
        write_line_for_index(index, f"{regiao}:", f"Concluído: {pokemon_hoenn}")
    await asyncio.sleep(0.2)
    return pokemon_hoenn

async def finalizar(pokemon_kanto, pokemon_johto, pokemon_hoenn):
    print("\n\nResultado final:")
    print(f"Seu trio pokemon é: {pokemon_kanto}, {pokemon_johto} e {pokemon_hoenn}")
    print("Obrigado por usar o processo de pokemon misterioso!")
    await asyncio.sleep(0.5)

async def main():
    global print_lock
    print_lock = asyncio.Lock()

    # tentar garantir que o terminal suporte ANSI (Windows 10+ normalmente ok)
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

    clear_screen()
    await menupokemon()
    await asyncio.sleep(0.5)

    # imprimimos as linhas iniciais do bloco (uma por região).
    # O cursor ficará logo abaixo do bloco; as funções usarão códigos ANSI relativos
    for reg in regioes_possiveis:
        print(f"{reg}:")  # linha reservada para cada região

    # cria tasks e usa gather para rodar concorrente
    start = time.perf_counter()
    task_kanto = asyncio.create_task(escolher_pokemon_kanto(0))
    task_johto = asyncio.create_task(escolher_pokemon_johto(1))
    task_hoenn = asyncio.create_task(escolher_pokemon_hoenn(2))

    # aguarda os três e captura retornos
    pokemon_kanto, pokemon_johto, pokemon_hoenn = await asyncio.gather(
        task_kanto, task_johto, task_hoenn
    )
    end = time.perf_counter()

    # após gather, imprimimos resultado final (abaixo do bloco)
    await finalizar(pokemon_kanto, pokemon_johto, pokemon_hoenn)
    print(f"\nTempo total de execução (concorrente): {end - start:.2f} segundos")

if __name__ == "__main__":
    asyncio.run(main())
