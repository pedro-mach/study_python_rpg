#npcs_list = [
#   {"name" : "Monstro-Fraco", "level": 1, "type": "Fire"},
#   {"name" : "Monstro-Forte", "level": 3,"type": "Water"},
#   {"name" : "Monstro-Magico", "level": 5,"type": "Ice"},
#   {"name" : "Monstro-Gigante", "level": 9, "type": "Void"},
#   {"name" : "Monstro-Dragao", "level": 15, "type": "Darkness"}  # Adicionando novos NPCs
#]

#for npc in npcs_list:
#    print(npc["type"])
from random import randint
import os
import sys
import time

def reset():
    python = sys.executable
    os.execl(python, python, *sys.argv)

npc_list = []

#variaveis de armadura e classe
#armadura = dano - 10
    # Solicita o nome
nome = input("Digite o nome: ")
continuar = input("Digite 'TANK' para +10 de Armadura, 'ASSASINO' para +10 de dano ou 'NENHUM' para jogar: ")
level = 1
dano_player = (level + (randint(10, 15)))*2
hp = 50 *(randint(2, 5)/2)
if continuar.upper() == "ASSASINO":
        dano_player += 10
Player = {     
    "nome": nome,
    "level": 1,
    "exp": 0,
    "exp_max": 30,
    "hp": hp,
    "hp_max": hp,
    "dano": dano_player,
    "classe": continuar
    }
   
print(
        f"Nome: {Player['nome']} | Level: {Player['level']} | HP: {Player['hp']} | Damage: {Player['dano']} | Classe: {Player['classe']}"
    )

def create_npc():
    level = randint(1, 30) # level
    if level <= 10: #raridade
        raridade = "Comum"
    elif level <= 18:
        raridade = "Raro"
    elif level <= 25:
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

    x = len(npc_list) + 1  # Contador para nomear os NPCs automaticamente.
    
    new_npc = { # criação de NPCs e atribuições
        "Nome": f"NPC #{x}",
        "Level": level,
        "Dano": dano_original,
        "damage": dano, 
        "hp": 50 *(level/2), # var de hp - mudar
        "exp": (dano - level)*2,
        "Raridade": raridade,
        "Class": Classe
        }
    
    return new_npc

def rep_npc(n_npcs): # adiciona na lista
    for x in range(n_npcs):
        npc = create_npc()
        npc_list.append(npc)
    
def show_npcs(): # fromatação
    for npc in npc_list:
        print(
            f"Nome: {npc['Nome']} | Level: {npc['Level']} | HP: {npc['hp']} | Dano-origal: {npc['Dano']} | Dano: {npc['damage']} | Classe: {npc['Class']} | Raridade: {npc['Raridade']} | XP: {npc['exp']}"
        )
rep_npc(5)

def select():
    show_npcs()
    while True:
        try:
            npc = int(input("Escolha um NPC: "))
            if  npc >= 0 and  npc <= len(npc_list):
                return npc_list[npc - 1]
            else:
                print("Escolha um NPC válido!")
        except ValueError:
            print("Escolha um NPC válido!")
                
def final():
    npc = select()
    Player['exp'] += npc['exp']
    if Player['exp'] >= Player['exp_max']:
        Player['level'] += 1
        Player['exp'] -= Player['exp_max']
        Player['exp_max'] = 30 + (Player['level'] * 10)
        Player['hp_max'] += 50
        Player['hp'] = Player['hp_max']
        print(f"Level Up! Novo Level: {Player['level']}")   
        
def batalha():
    npc = select()
    while Player['hp'] > 0 and npc['hp'] > 0:
            Player['hp'] -= npc['damage']
            npc['hp'] -= Player['dano']
            print(
                f"Nome: {Player['nome']} | HP: {Player['hp']} | Damage: {Player['dano']}"
            )
            print(
                f"Nome: {npc['Nome']} | HP: {npc['hp']} | Damage: {npc['damage']}"
            )
    if npc['hp'] < 0:
        npc_list.remove(npc)
        print(f"NPC derrotado || Exp Ganha:{npc['exp']}")
        final()
        Player['exp'] += npc['exp']
        Player['hp'] = Player['hp_max']
        print( f"Nome: {Player['nome']} | Level: {Player['level']} | HP: {Player['hp']}")
        select()
        batalha()
        
    if Player['hp'] < 0:
        print(f"Você foi derrotado !!!")
        print("Vamos novamente?")
        continuar = input("Digite 'S' para continuar ou 'N' para sair: ")
        if continuar.upper() == "S":
            print("Vamos nessa então !!!")
            time.sleep(3)
            reset()
        else:
            print("Saindo do Jogo...")
            time.sleep(3)
            sys.exit()
batalha()

   