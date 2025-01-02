#Jogo de RPG-Terminal feito em Python por Matheus Pereira Alves
#Agradecimentos ao DEV/Youtuber Baober pelas dicas e ensinamentos

import os
import random
import time
import sys
import textwrap
import cmd

q2 = 0

#Classe do Jogador
class Player:
    def __init__(self):
        #Atributos do jogador
        self.name = ''
        self.luck = 0
        self.theory  = 0
        self.resiliency = 0
        self.practice = 0

        #Efeitos do jogador
        self.energy = 100
        self.hunger = 0
        self.stress = 0
        self.concentration = 100

        #Dinheiro do jogador
        self.gold = 0

        #Localização do jogador
        self.location = 'Casa'

        #Estado do jogador
        self.gameover = False

#Instância do jogador
myPlayer = Player()

### Função para desenhar uma linha ###
def draw_line():
    print('----------------------------------------------') #Desenha uma linha

### Função para as opções do menu principal ###
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("jogar"):
        start_game()
    elif option.lower() == ("ajuda"):
        help_menu()
    elif option.lower() == ("sair"):
        sys.exit()
    while option.lower() not in ['jogar', 'ajuda', 'sair']:
        print("Por favor, insira uma opção válida.")
        option = input("> ")
        if option.lower() == ("jogar"):
            start_game()
        elif option.lower() == ("ajuda"):
            help_menu()
        elif option.lower() == ("sair"):
            sys.exit()

### Função para o menu principal ###
def title_screen():
    os.system('clear')
    draw_line()
    print("----------# Tales of an Engineer #-----------")
    draw_line()
    print("                         - Jogar -                           ")
    print("                         - Ajuda -                           ")
    print("                         - Sair -                            ")
    title_screen_selections()

### Função para o menu de ajuda ###
def help_menu():
    os.system('clear')
    draw_line()
    print("Bem-vindo ao menu de ajuda!")
    print("O jogo é um RPG de texto, onde você deve tomar decisões para sobreviver no terrível mundo da engenharia.")
    print("Você se movimenta pelo mapa digitando em qual lugar você quer ir no momento. Por exemplo 'Casa'.")
    time.sleep(5)
    title_screen()

### Mapa do jogo ###
# Casa - Sala de Estudos - Cantina - Biblioteca - Laboratório - Sala de Aula - Loja - Corredor #

map = {
    'casa': {
        'name': 'casa',
        'description': 'Você está em sua casa. O que deseja fazer?',
    },
    'sala de estudos': {
        'name': 'sala de estudos',
        'description': 'Um ambiente silencioso ideal para estudos em grupo ou individual. O equilíbro entre teoria e prática',
    },
    'cantina': {
        'name': 'cantina',
        'description': 'A cantina é um lugar para comer e relaxar. Você pode comprar comida e bebida aqui.',
    },
    'biblioteca': {
        'name': 'biblioteca',
        'description': 'A biblioteca é um lugar para estudar e pesquisar. Quem sabe você não ache algo aqui.',
    },
    'laboratório': {
        'name': 'laboratório',
        'description': 'O laboratório é um lugar para experimentos e práticas. O melhor lugar para se aprender na prática.',
    },
    'sala de aula': {
        'name': 'sala de aula',
        'description': 'A sala de aula é o lugar perfeito para entender a teoria.',
    },
    'loja': {
        'name': 'loja',
        'description': 'A loja é um lugar para comprar itens e equipamentos.',
    },
    'corredor': {
        'name': 'corredor',
        'description': 'O corredor é um lugar de passagem entre os ambientes da universidade. Quem sabe você não encontra alguém interessante por aqui.',
    },
}

### Interatividade do jogo ###
def print_location():
    print('\n' + 'Você está em: ' + myPlayer.location)
    print(map[myPlayer.location]['description'])

def prompt():
    draw_line()
    print("O que você deseja fazer?")
    print("Mover - Interagir - Estudar - Comer - Descansar - Status - Sair")
    action = input("> ")
    acceptable_actions = ['mover', 'interagir', 'estudar', 'comer', 'descansar', 'status']
    while action.lower() not in acceptable_actions:
        print("Ação inválida. Por favor, insira uma ação válida.")
        action = input("> ")
    if action.lower() == 'sair':
        sys.exit()
    elif action.lower() == 'mover':
        player_move()
    elif action.lower() == 'interagir':
        player_interact()
    elif action.lower() == 'estudar':
        player_study()
    elif action.lower() == 'comer':
        player_eat()
    elif action.lower() == 'descansar':
        player_rest()
    elif action.lower() == 'status':
        player_status()
    
def player_move():
    ask = input("Para onde você deseja ir? ").lower()
    if ask in map:
        myPlayer.location = ask
        print_location()
    else:
        print("Local inválido. Tente novamente.")
    
def  player_interact():
    print("Você interagiu com o ambiente.")

def player_study():
    print("Você estudou.")

def player_eat():
    print("Você comeu.")

def  player_rest():
    print("Você descansou.")

def player_status():
    print("Seus status são:")
    print("Energia: " + str(myPlayer.energy))
    print("Fome: " + str(myPlayer.hunger))
    print("Estresse: " + str(myPlayer.stress))
    print("Concentração: " + str(myPlayer.concentration))
    print("Ouro: " + str(myPlayer.gold))

### Funcionalidade do jogo ###
def start_game():
    setup_game()
    main_game_loop()

def main_game_loop():
    while myPlayer.gameover is False:
        prompt()

# Status do Player #
def player_class():
    if q2 == '1':
        myPlayer.luck = 1
        myPlayer.theory = 3
        myPlayer.resiliency = 3
        myPlayer.practice = 3
    elif q2 == '2':
        myPlayer.luck = 1
        myPlayer.theory = 4
        myPlayer.resiliency = 1
        myPlayer.practice = 4
    elif q2 == '3':
        myPlayer.luck = 1
        myPlayer.theory = 2
        myPlayer.resiliency = 2
        myPlayer.practice = 5
    elif q2 == '4':
        while myPlayer.luck + myPlayer.theory + myPlayer.resiliency + myPlayer.practice != 10:
            myPlayer.luck = random.randint(1, 3)
            myPlayer.theory = random.randint(1, 4)
            myPlayer.resiliency = random.randint(1, 4)
            myPlayer.practice = random.randint(1, 4)

def setup_game():
    
    os.system('clear')

    question1 = "Qual é o seu nome?"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    myPlayer.name = input("> ")
    question2 = "Qual será sua classe?\n1 - Dedicado\n2 - Talento Natural\n3 - Mão na Massa\n4 - Aleatório\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    q2 = (input(""))
    player_class()

    #Introdução
    s1 = "Bem-vindo, " + myPlayer.name + ". Você agora irá iniciar sua jornada como um engenheiro, boa sorte!" #s1 = speech 1
    s2 = "Prepare-se para enfrentar inimigos formidáveis e conseguir aprimorar seus conhecimentos e habilidades!"
    s3 = "Aposto que você não consegue sobreviver até o final... MUHAHAHAHA!"

    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    print("\n")
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    print("\n")
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(1.8)
    print("\n")

    os.system('clear')




title_screen()

