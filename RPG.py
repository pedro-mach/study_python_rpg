
from random import randint
import os
import sys
import time

def reset():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def space():
    print("◼" * 100)

print()
space()
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
time.sleep(0.3)
print("░░█░░░░█▀▀▀█░█▀▀█░█▀▀▄░▀█▀░█▄░░█░█▀▀█░░")
time.sleep(0.3)
print("░░█░░░░█░░░█░█▄▄█░█░░█░░█░░█░█░█░█░▄▄░░")
time.sleep(0.3)
print("░░█▄▄█░█▄▄▄█░█░░█░█▄▄▀░▄█▄░█░░▀█░█▄▄█░░")
time.sleep(0.3)
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
time.sleep(0.3)
print("░█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█░")
time.sleep(0.3)
print("░█░██░██░██░██░██░██░██░██░██░██░██░░█░")
time.sleep(0.3)
print("░█░██░██░██░██░██░██░██░██░██░██░██░░█░")
time.sleep(0.3)
print("░█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█░")
time.sleep(0.3)
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
space()

npc_list = []

print("→ Vamos começar criando seu player")
nome = input("Digite o nome: ") # Solicita o nome
print("→ Vamos escolher uma classe!!")
continuar = input("Digite 'TANK' para +10 de Armadura, 'ASSASSINO' para +10 de dano ou 'NENHUM' para jogar: ")
level = 1
dano_player = (level + (randint(10, 15)))*2
hp = 50 *(randint(2, 5)/2)
if continuar.upper() == "TANK":
    hp = hp + 50
if continuar.upper() == "ASSASSINO":
    dano_player += 10
Player = {     
    "nome": nome,
    "level": 1,
    "exp": 0,
    "exp_max": 20,
    "hp": hp,
    "hp_max": hp,
    "dano": dano_player,
    "classe": continuar
    }
space()

print(
        f"Player: {Player['nome']} | Level: {Player['level']} | HP: {Player['hp']} | Damage: {Player['dano']} | Classe: {Player['classe']}"
    )
space()
    

def create_npc():
    level = randint(1, 20) # level
    if level <= 10: #raridade
        raridade = "Comum"
    elif level <= 16:
        raridade = "Raro"
    elif level <= 19:
        raridade = "Epico"
    else:
        raridade = "Lendario"
        
    damage_var = randint(1, 10) # Define variavel dano
    dano = 2 * (level + damage_var) # dafine dano
    dano_original = dano
    if dano <= 30: # verifica força
        Classe = "Fraco"
    elif dano <= 55:
        Classe = "Medio"
    elif dano <= 70:
        Classe = "Forte"
    else:
        Classe = "Elite"
    
    if continuar.upper() == "TANK":
        dano -= 10
    if dano <= 0:
        dano = 0
  # Contador para nomear os NPCs automaticamente.
    
    exp = (dano_original)*2
    if exp <=0:
        exp = 0
    
    nome = len(npc_list) + 1
    new_npc = { # criação de NPCs e atribuições
        "Nome": nome,
        "Level": level,
        "Dano": dano_original,
        "damage": dano, 
        "hp": 40 *(level/2), # var de hp - mudar
        "exp": exp,
        "Raridade": raridade,
        "Class": Classe
        }
    
    return new_npc

def rep_npc(n_npcs): # adiciona na lista
    for x in range(n_npcs):
        npc = create_npc()
        npc_list.append(npc)

rep_npc(5)

print("Selecione um NPC pelo ID para iniciar o combate")
print("↓↓↓")

def show_npcs(): # fromatação
    for npc in npc_list:
        if npc['hp'] > 0:
            print(
            f"ID {npc['Nome']} | Level: {npc['Level']} | HP: {npc['hp']} | Dano-origal: {npc['Dano']} | Dano: {npc['damage']} | Classe: {npc['Class']} | Raridade: {npc['Raridade']} | XP: {npc['exp']}"
            )
        else:
            print(
               f"ID {npc['Nome']} | NPC Morto"
            )

def select():
    show_npcs()
    npc = int(input("Escolha um NPC: "))
    if  0 <= npc <= 5:
                return npc_list[npc - 1]
    else:
        print("Escolha um NPC válido!")
        space()
        select()
        
    
                
def final():
    if Player['exp'] >= Player['exp_max']:
        Player['level'] += 1
        Player['exp'] -= Player['exp_max']
        Player['exp_max'] =30 
        Player['hp_max'] += 50
        Player['hp'] = Player['hp_max']
        print(f"→Level Up! Novo Level: {Player['level']}")   
        
def batalha():
    npc = select()
    space()
    while Player['hp'] > 0 and npc['hp'] > 0:
            Player['hp'] -= npc['damage']
            npc['hp'] -= Player['dano']
            print(
                f"Nome: {Player['nome']} | HP: {Player['hp']} | Damage: {Player['dano']}"
            )
            print(
                f"Nome: {npc['Nome']} | HP: {npc['hp']} | Damage: {npc['damage']}"
            )
            time.sleep(0.5)
    space()
    if npc['hp'] < 0:
        Player['exp'] += npc['exp']
        print(f"→ NPC derrotado || Exp Ganha:{npc['exp']}")
        final()
        Player['hp'] = Player['hp_max']
        space()
        print( f"Nome: {Player['nome']} | Level: {Player['level']} | HP: {Player['hp']} | Damage: {Player['dano']} | Exp: {Player['exp']} / {Player['exp_max']}")
        space()
        print("Selecione um NPC pelo ID para iniciar o combate")
        print("↓↓↓")
        batalha()
        
    if Player['hp'] < 0:
        print(f"→ Você foi derrotado !!!")
        print("→ Vamos novamente?")
        continuar = input("Digite 'S' para continuar ou 'N' para sair: ")
        if continuar.upper() == "S":
            print("Vamos nessa então !!!")
            space()
            time.sleep(2)
            reset()
        else:
            print("Saindo do Jogo...")            
            space()
            time.sleep(0.3)
            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
            time.sleep(0.3)
            print("░░█░░░░█▀▀▀▀░█▀▀█░█░░█░█░█▄░░█░█▀▀█░░")
            time.sleep(0.3)
            print("░░█░░░░█◼◼◼░░█▄▄█░█░░█░█░█░█░█░█░▄▄░░")
            time.sleep(0.3)
            print("░░█▄▄█░█▄▄▄▄░█░░█░▀▄▄▀░█░█░░▀█░█▄▄█░░")
            time.sleep(0.3)
            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
            time.sleep(0.3)
            print("░█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█░")
            time.sleep(0.3)
            print("░█░██░██░██░██░██░██░██░██░██░██░░░█░")
            time.sleep(0.3)
            print("░█░██░██░██░██░██░██░██░██░██░██░░░█░")
            time.sleep(0.3)
            print("░█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█░")
            time.sleep(0.3)
            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
            space()
            time.sleep(2)
            sys.exit()
batalha()