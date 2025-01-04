#Jogo de RPG-Terminal feito em Python por Matheus Pereira Alves
#Agradecimentos ao DEV/Youtuber Baober pelas dicas e ensinamentos

import os
import random
import time
import sys

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

        #Dinheiro e itens do jogador
        self.gold = 0
        self.drink = 0
        self.food = 0
        self.calculator = False
        self.notebook = False
        self.multimeter = False

        #Localização do jogador
        self.location = 'casa'

        #Estado do jogador
        self.gameover = False

#Classe do Inimigo
class Enemy:
    pass

#Dicionário de Inimigos
mobs = {
    "Integral Tripla" : {
        "hp_min" : 12,
        "hp_max" : 16,
        "atk_min" : 2,
        "atk_max" : 4,
        "gold_min" : 5,
        "gold_max" : 10,
        "def_t" : 1,
        "def_p" : 1,
        "lines" : ["Você encontrou uma integral tripla! A lei de Ohm não vai te salvar agora...", "Você encontrou uma integral tripla! Bem que você deveria ter estudado coordenadas polares..."]
    },
    "EDO Homogênea" : {
        "hp_min" : 14,
        "hp_max" : 18,
        "atk_min" : 2,
        "atk_max" : 5,
        "gold_min" : 7,
        "gold_max" : 12,
        "def_t" : 2,
        "def_p" : 2,
        "lines" : ["Você encontrou uma EDO homogênea! A solução é trivial, eu acho...", "Uma EDO Homogênea, sério, quem resolve algo por EDO?"]
    },
    "Circuito de Primeira Ordem" : {
        "hp_min" : 18,
        "hp_max" : 22,
        "atk_min" : 3,
        "atk_max" : 5,
        "gold_min" : 10,
        "gold_max" : 15,
        "def_t" : 3,
        "def_p" : 6,
        "lines" : ["Você encontrou um circuito de primeira ordem! Dá pra fazer isso por EDO?", "Você encontrou um circuito de primeira ordem! O Tau significa o que mesmo?"]
    },
    "Transformada de Laplace" : {
        "hp_min" : 24,
        "hp_max" : 28,
        "atk_min" : 4,
        "atk_max" : 6,
        "gold_min" : 15,
        "gold_max" : 20,
        "def_t" : 4,
        "def_p" : 9,
        "lines" : ["Você encontrou uma Transformada de Laplace! Mais assustadora que descobrir um polo no semi-plano direito!", "Transformada de Laplace à vista! Prepare-se para ser convertido em frações parciais!"]
    },
    "Filtro rejeita-faixas de 4 Ordem" : {
        "hp_min" : 30,
        "hp_max" : 34,
        "atk_min" : 5,
        "atk_max" : 7,
        "gold_min" : 20,
        "gold_max" : 25,
        "def_t" : 11,
        "def_p" : 5,
        "lines" : ["Você encontrou um filtro rejeita-faixas de 4ª ordem! Eu realmente não queria ser você agora...", "Você encontrou um filtro rejeita-faixas de 4ª ordem! Boa sorte tentando ajustar a frequência de corte!"]
    },
    "Motor Assíncrono em Delta" : {
        "hp_min" : 36,
        "hp_max" : 40,
        "atk_min" : 6,
        "atk_max" : 8,
        "gold_min" : 25,
        "gold_max" : 30,
        "def_t" : 14,
        "def_p" : 6,
        "lines" : ["Você encontrou um motor assíncrono em delta! Quem em sã consciência me chamaria de Motor de Corrente Contínua", "Você encontrou um motor assíncrono em delta! Qual a chance de ter um esquilo dentro dele?"]
    }

}

#Dicionário de Bosses
bosses = {
    "Prova de Máquinas Elétricas" : {
        "hp_min" : 150,
        "hp_max" : 250,
        "atk_min" : 10,
        "atk_max" : 20,
        "gold_min" : 100,
        "gold_max" : 300,
        "def_t" : 15,
        "def_p" : 25,
        "lines" : ["A Prova de Máquinas Elétricas Começa!", "Você estudou Ciclo de Rankine? KKKKKKKKKKK boa sorte!"]
    },
    "Prova de Sistema Elétrico de Potência" : {
        "hp_min" : 200,
        "hp_max" : 220,
        "atk_min" : 14,
        "atk_max" : 18,
        "gold_min" : 200,
        "gold_max" : 250,
        "def_t" : 12,
        "def_p" : 45,
        "lines" : ["A Prova de Máquinas Elétricas Começa!", "Você estudou Ciclo de Rankine? KKKKKKKKKKK boa sorte!"]
    },
        
}

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
    print("----------# Tales of an Engineer #------------")
    draw_line()
    print("                 - Jogar -                           ")
    print("                 - Ajuda -                           ")
    print("                 - Sair -                            ")
    title_screen_selections()

### Função para o menu de ajuda ###
def help_menu():
    os.system('clear')
    draw_line()
    print("Bem-vindo ao menu de ajuda!")
    print("O jogo é um RPG de texto, onde você deve tomar decisões para sobreviver no terrível mundo da engenharia.")
    print("Você se movimenta pelo mapa digitando em qual lugar você quer ir no momento. Por exemplo 'Casa'.")
    print("Cuidado ao estudar no laboratório sem preparo kkk")
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
        'description': 'Um ambiente silencioso ideal para estudos em grupo ou individual. Se quiser aprender na prática, é aqui',
    },
    'cantina': {
        'name': 'cantina',
        'description': 'A cantina é um lugar para comer e relaxar. Você pode comprar comida e bebida aqui.',
    },
    'laboratório': {
        'name': 'laboratório',
        'description': 'O laboratório é um lugar para experimentos e práticas. Cuidado para não estudar por aqui sem estar devidamente preparado',
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

#Listas NPC
#NPC - Casa
npc_casa = ["Você ja estudou o assunto? por mim adiava essas provas!", "Esqueci de colocar o frango pra descongelar kkkkkkkkkkkkkk", "Moço que professor panguão esse professor viu..."]
npc_sala_de_estudos = ["O Ar-condicionado ta fuleiro viu kkkkkkk", "Será que vai ter o décimo terceiro do auxílio?", "Eu to ficando doido ou tem um cachorro no laboratório?"] #kkkkkkkk o copilot que recomendou a 3 fala kkkkkkkk
npc_laboratorio = ["To conseguindo ler nada, deve ser a glicose kkkk", "Bora botar esse motor pra ligar aqui", "Olha quem chegou rapaz HAHAHA"] #vou nem falar em quem foi inspirado
npc_sala_de_aula = ["Por mim em vez de prova tinha que fazer um trabalho", "Vou emendar o feriado da quinta com a sexta e voltar pra casa kkkk", "To entendendo é nada, vou meter é o decoras"]


### Interatividade do jogo ###
def print_location():
    print('\n' + 'Você está em: ' + myPlayer.location)
    print(map[myPlayer.location]['description'])

def prompt():
    draw_line()
    print("O que você deseja fazer?")
    print("Mover - Interagir - Estudar - Comer - Descansar - Status - Sair")
    action = input("> ")
    acceptable_actions = ['mover', 'interagir', 'estudar', 'comer', 'descansar', 'status', 'sair']
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
    elif action.lower() == 'sair':
        sys.exit()
    
def player_move():
    os.system('clear')
    print("Possíveis locais: Casa - Sala de Estudos - Cantina - Laboratório - Sala de Aula - Loja - Corredor")
    ask = input("Para onde você deseja ir?\n>").lower()
    if ask in map:
        myPlayer.location = ask
        print_location()
    else:
        print("Local inválido. Tente novamente.")
    
def  player_interact():
    print("Você interagiu com o ambiente.")
    interaction = interactions.get(myPlayer.location, interact_default)
    interaction()

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
    print("Seus atributos são:")
    print("Sorte: " + str(myPlayer.luck))
    print("Teoria: " + str(myPlayer.theory))
    print("Resiliência: " + str(myPlayer.resiliency))
    print("Prática: " + str(myPlayer.practice))
    print("Seus itens e gold são:")
    print("Ouro: " + str(myPlayer.gold))
    print("Pastéis: " + str(myPlayer.food))
    print("Cafés: " + str(myPlayer.drink))
    print("Calculadora: " + str(myPlayer.calculator))
    print("Notebook: " + str(myPlayer.notebook))
    print("Multímetro: " + str(myPlayer.multimeter))


### Funcionalidade do jogo ###
def start_game():
    setup_game()
    main_game_loop()

def main_game_loop():
    while myPlayer.gameover is False:
        prompt()

#Funções de interações
def interact_casa():
    fala = "Colega de quarto: " + random.choice(npc_casa) + "\n"
    for character in fala:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)

def interact_sala_de_estudos():
    fala = "Estudante descabelado: " + random.choice(npc_sala_de_estudos) + "\n"
    for character in fala:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)

def interact_cantina():
    fala = "O que você quer comprar?\nOs preços são:\nPastel - 10\nCafé - 5\nCaso não queira comprar, digite algo diferente.\n"
    for character in fala:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    compra = input("> ")
    if compra.lower() == 'pastel':
        if myPlayer.gold >= 10:
            myPlayer.gold -= 10
            myPlayer.food += 1
            print("Você comprou um pastel.")
        else:
            print("Você não tem dinheiro suficiente.")
    elif compra.lower() == 'café':
        if myPlayer.gold >= 5:
            myPlayer.gold -= 5
            myPlayer.drink += 1
            print("Você comprou um café.")
        else:
            print("Você não tem dinheiro suficiente.")
    else:
        print("Você não comprou nada.")

def interact_laboratorio():
    fala = "Professor Gente Boa: " + random.choice(npc_laboratorio) + "\n"
    for character in fala:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)

def interact_sala_de_aula():
    fala = "Aluno Agoniado: " + random.choice(npc_sala_de_aula) + "\n"
    for character in fala:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)

def interact_loja():
    fala = "O que você vai querer comprar?\nOs preços são:\nCalculadora - 100\nMultímetro - 100\nNotebook - 200\nCaso não queira comprar, digite algo diferente.\n"
    for character in fala:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    compra = input("> ")
    if compra.lower() == 'calculadora':
        if myPlayer.calculator is True:
            print("Você já tem uma calculadora.")
        else:
            if myPlayer.gold >= 100:
                myPlayer.gold -= 100
                myPlayer.calculator = True
                print("Você comprou uma calculadora.")
            else:
                print("Você não tem dinheiro suficiente.")
    elif compra.lower() == 'notebook':
        if myPlayer.notebook is True:
            print("Você já tem um notebook.")
        else:
            if myPlayer.gold >= 200:
                myPlayer.gold -= 200
                myPlayer.notebook = True
                print("Você comprou um notebook.")
            else:
                print("Você não tem dinheiro suficiente.")
    elif compra.lower() == 'multímetro':
        if myPlayer.multimeter is True:
            print("Você já tem um multímetro.")
        else:
            if myPlayer.gold >= 100:
                myPlayer.gold -= 100
                myPlayer.multimeter = True
                print("Você comprou um multímetro.")
            else:
                print("Você não tem dinheiro suficiente.")
    else:
        print("Você não comprou nada.")

def interact_corredor():
    rng = random.randint(1, 50)
    if rng == 50:
        fala = "Auf Auf... disse o cachorro que apareceu no corredor.\n"
        for character in fala:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.04)
        myPlayer.gold += 100
        myPlayer.energy = 100
        myPlayer.hunger = 0
        myPlayer.stress = 0
        myPlayer.concentration = 100
        myPlayer.luck += 5
        myPlayer.theory += 5
        myPlayer.resiliency += 5
        myPlayer.practice += 5
        fala = "Você ganhou a benção do doguinho! Ele te deu 100 de ouro e te deu um boost de status!\n"
        for character in fala:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.04)
    else:
        fala = "Você não encontrou nada de muito interessante no corredor\n"
        for character in fala:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.04)


def interact_default():
    pass

#Dicionário de localizações-interação
interactions = {
    'casa' : interact_casa,
    'sala de estudos' : interact_sala_de_estudos,
    'cantina' : interact_cantina,
    'laboratório' : interact_laboratorio,
    'sala de aula' : interact_sala_de_aula,
    'loja' : interact_loja,
    'corredor' : interact_corredor,
}

# Status do Player #
def player_class(q2):
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
    q2 = input("> ")
    player_class(q2)
    while q2 not in ['1', '2', '3', '4']:
        print("Por favor, insira uma opção válida.")
        q2 = input("> ")
        player_class(q2)

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

