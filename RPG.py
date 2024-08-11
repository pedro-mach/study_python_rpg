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

npc_list = []

start_level = 1
dano_player = (start_level + (randint(10, 15)))*2,
Player = {
    "nome": "Pedro",
    "level": 1,
    "exp": 0,
    "exp_max": 30,
    "hp": 80,
    "hp_max": 200,
    "dano": dano_player
}
print (Player
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
    if dano <= 30: # verifica força
        Classe = "Fraco"
    elif dano <= 55:
        Classe = "Medio"
    elif dano <= 70:
        Classe = "Forte"
    else:
        Classe = "Elite"

    x = len(npc_list) + 1  # Contador para nomear os NPCs automaticamente.
    
    new_npc = { # criação de NPCs e atribuições
        "Nome": f"NPC #{x}",
        "Level": level,
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
            f"Nome: {npc['Nome']} | Level: {npc['Level']} | HP: {npc['hp']} | Damage: {npc['damage']} | Classe: {npc['Class']} | Raridade: {npc['Raridade']} | XP: {npc['exp']}"
        )
    
rep_npc(5) # quantia
show_npcs() # lista

    