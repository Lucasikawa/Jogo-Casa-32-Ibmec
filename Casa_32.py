import random

current_player = 0
turn_counter = 1

def __game__():

    global dice
    global right
    global wrong
    global step_counts
    global game_dif
    global num_players
    global current_player
    global turn_counter
    global players_list
    global player_position

    # 2) Inicia o jogo com uma jogada de dado que é randomizada pelo algoritmo

    while True:
        if current_player == 0:
            print(f'\n--- Turno {turn_counter} ---')

        print(f"\nRodada do jogador {players_list[current_player]}.")
        enter = input('Pressione [ENTER] para rolar o dado.')

        if players_list[0] and players_list[1] not in step_counts:
            step_counts[players_list[0]] = 0
            step_counts[players_list[1]] = 0

        if players_list[0] and players_list[1] not in right:
            right[players_list[0]] = 0
            right[players_list[1]] = 0

        if players_list[0] and players_list[1] not in wrong:
            wrong[players_list[0]] = 0
            wrong[players_list[1]] = 0

        # 2) a) O algoritmo mostra o valor obtido pelo dado​
        dice = random.choice(range(1, 7))
        print(f'\nO jogador {players_list[current_player]} tirou {dice} no dado.')

        if player_position[current_player] + dice < 32:
            print(f'Para prosseguir para a casa {player_position[current_player] + dice} o jogador deve responder corretamente a senguinte questão.')
        else:
            print('Para prosseguir para a casa final o jogador deve responder a seguinte questão.')

        # 3) Para as perguntas:
        if game_dif == 'FACIL' or game_dif == 'FÁCIL':
            choose = 1
        elif game_dif == 'MEDIO' or game_dif == 'MÉDIO':
            choose = random.randint(1, 2)
        elif game_dif == 'DIFICIL' or game_dif == 'DIFÍCIL':
            choose = random.randint(1, 3)

        if choose == 1:
            easy_qstn(dice)
        elif choose == 2:
            med_qstn(dice)
        elif choose == 3:
            hard_qstn()

        if player_position[current_player] < 32:
            current_player = (current_player + 1) % num_players

            if current_player == 0:
                turn_counter += 1

        else:
            #  verifica se atingiu a casa 32, se sim imprime mensagem "parabéns".
            #  O algoritmo mostra o ranqueamento (matriz):
            #     1.quantidade de casas andadas​(dicionário)​​
            #     2.quantidade de acertos​(dicionário)​​
            #     3.quantidade de erros​(dicionário)

            matriz =  [
                  ["jogador", "acertos", "erros", "casas andadas", "casas regredidas"],
                  [players_list[0], right[players_list[0]], wrong[players_list[0]], step_counts[players_list[0]], wrong[players_list[0]]],
                  [players_list[1], right[players_list[1]], wrong[players_list[1]], step_counts[players_list[1]], wrong[players_list[1]]]
                      ]

            print(f'\nParabéns! O jogador {players_list[current_player]} chegou a casa final.', "\n")

            print("+-----------------+---------+-------+-----------------+-------------------+")
            print("| {:<15} | {:^7} | {:^5} | {:<15} | {:<17} |".format(matriz[0][0], matriz[0][1], matriz[0][2], matriz[0][3], matriz[0][4]))
            print("+-----------------+---------+-------+-----------------+-------------------+")
            for linha in matriz[1:]:
                print("| {:<15} | {:^7} | {:^5} | {:^15} | {:^17} |".format(linha[0], linha[1], linha[2], linha[3], linha[4]))
            print("+-----------------+---------+-------+-----------------+-------------------+")

            break

def easy_qstn(dice_num):

    global player_position
    global right
    global wrong
    global step_counts

    # 3) a) é randomizado dois números para operações (à randomização é diferente)
    # 3) b) para tipo de pergunta no nível é randomizado um número
    # 3. Logo, se certo: aumenta uma unidade no número de acertos, se errado: aumenta uma unidade no números de erros. O número de casas também é "contado"
    choice = random.choice(range(1, 3))
    num_00, num_01 = random.choice(range(0, 31)), random.choice(range(0, 31))

    # 3) c. solicita a resposta e verifica:​
    if choice == 1:
        answer = int(input(f'Qual o resultado da expressão {num_00} + {num_01}?\n\nResposta: '))
        # Se a resposta estiver correta, a posição do jogador aumenta com o número que está no dado e o algoritmo mostra a nova posição. ​
        if num_00 + num_01 == answer:
            step_counts[players_list[current_player]] += dice_num
            right[players_list[current_player]] += 1
            print('\nParabéns! Você acertou a pergunta!')
            player_position[current_player] += dice_num
            if player_position[current_player] < 32:
                print(f'Você prosseguiu para a casa {player_position[current_player]}.')
            else:
                # verifica se atingiu a casa 32, se sim imprime mensagem "parabéns".​
                print('Parabéns! Você chegou a casa final.')
        else:
            # Se a resposta estiver errada a posição diminui um, se não for a posição 0
            print('\nDesculpe! Sua resposta está incorreta. Retorne uma casa.')
            if player_position[current_player] != 0:
                player_position[current_player] -= 1
            print(f'Você voltou para a casa {player_position[current_player]}')
            wrong[players_list[current_player]] += 1

    # 3) c. solicita a resposta e verifica:​
    elif choice == 2:
        if num_00 < num_01:
            num_00, num_01 = num_01, num_00
        answer = int(input(f'Qual o resultado da expressão {num_00} - {num_01}?\n\nResposta: '))
        # Se a resposta estiver correta, a posição do jogador aumenta com o número que está no dado e o algoritmo mostra a nova posição.
        if num_00 - num_01 == answer:
            step_counts[players_list[current_player]] += dice_num
            right[players_list[current_player]] += 1
            print('\nParabéns! Você acertou a pergunta!')
            player_position[current_player] += dice_num
            if player_position[current_player] < 32:
                print(f'Você prosseguiu para a casa {player_position[current_player]}.')
            else:
                # verifica se atingiu a casa 32, se sim imprime mensagem "parabéns".​
                print('Parabéns! Você chegou a casa final.')
        else:
            # Se a resposta estiver errada a posição diminui um, se não for a posição 0
            print('\nDesculpe! Sua resposta está incorreta. Retorne uma casa.')
            if player_position[current_player] != 0:
                player_position[current_player] -= 1
            print(f'Você voltou para a casa {player_position[current_player]}')
            wrong[players_list[current_player]] += 1


def med_qstn(dice_num):

    global player_position
    global right
    global wrong
    global step_counts

    # 3) a) é randomizado dois números para operações (à randomização é diferente)
    # 3) b) para tipo de pergunta no nível é randomizado um número
    # 3. Logo, se certo: aumenta uma unidade no número de acertos, se errado: aumenta uma unidade no números de erros. O número de casas também é "contado"
    choice = random.choice(range(1, 3))
    num_00, num_01 = random.choice(range(0, 31)), random.choice(range(0, 31))

    # 3) c. solicita a resposta e verifica:​
    if choice == 1:
        # Se a resposta estiver correta, a posição do jogador aumenta com o número que está no dado e o algoritmo mostra a nova posição.
        answer = int(input(f'Qual o resultado da expressão {num_00} * {num_01}?\n\nResposta: '))
        if num_00 * num_01 == answer:
            step_counts[players_list[current_player]] += dice_num
            right[players_list[current_player]] += 1
            print('\nParabéns! Você acertou a pergunta!')
            player_position[current_player] += dice_num
            if player_position[current_player] < 32:
                print(f'Você prosseguiu para a casa {player_position[current_player]}.')
            else:
                # verifica se atingiu a casa 32, se sim imprime mensagem "parabéns".​
                print('Parabéns! Você chegou a casa final.')
        else:
            # Se a resposta estiver errada a posição diminui um, se não for a posição 0
            print('\nDesculpe! Sua resposta está incorreta. Retorne uma casa.')
            if player_position[current_player] != 0:
                player_position[current_player] -= 1
            print(f'Você voltou para a casa {player_position[current_player]}')
            wrong[players_list[current_player]] += 1

    # 3) c. solicita a resposta e verifica:​
    elif choice == 2:
        num_00 = random.choice(range(2, 65, 2))
        answer = int(input(f'Qual o resultado da expressão {num_00} / 2?\n\nResposta: '))
        # Se a resposta estiver correta, a posição do jogador aumenta com o número que está no dado e o algoritmo mostra a nova posição.
        if num_00 / 2 == answer:
            step_counts[players_list[current_player]] += dice_num
            right[players_list[current_player]] += 1
            print('\nParabéns! Você acertou a pergunta!')
            player_position[current_player] += dice_num
            if player_position[current_player] < 32:
                print(f'Você prosseguiu para a casa {player_position[current_player]}.')
            else:
                # verifica se atingiu a casa 32, se sim imprime mensagem "parabéns".​
                print('Parabéns! Você chegou a casa final.')
        else:
            # Se a resposta estiver errada a posição diminui um, se não for a posição 0
            print('\nDesculpe! Sua resposta está incorreta. Retorne uma casa.')
            if player_position[current_player] != 0:
                player_position[current_player] -= 1
            print(f'Você voltou para a casa {player_position[current_player]}')
            wrong[players_list[current_player]] += 1

def hard_qstn():

    square_root = [1, 4, 9, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]

    global player_position
    global right
    global wrong
    global step_counts
    global dice

    # 3) a) é randomizado dois números para operações (à randomização é diferente)
    # 3) b) para tipo de pergunta no nível é randomizado um número
    # 3. Logo, se certo: aumenta uma unidade no número de acertos, se errado: aumenta uma unidade no números de erros. O número de casas também é "contado"
    num_00, num_01 = random.choice(range(1, 11)), random.choice(range(1, 4))
    choice = random.choice(range(1, 3))
    square = random.choice(square_root)

    # 3) c. solicita a resposta e verifica:​
    if choice == 1:
        answer = int(input(f'Qual o resultado da expressão {num_00} *[elevado]* {num_01}?\n\nResposta: '))
        # Se a resposta estiver correta, a posição do jogador aumenta com o número que está no dado e o algoritmo mostra a nova posição.
        if num_00 ** num_01 == answer:
            step_counts[players_list[current_player]] += dice
            right[players_list[current_player]] += 1
            print('\nParabéns! Você acertou a pergunta!')
            player_position[current_player] += dice
            if player_position[current_player] < 32:
                print(f'Você proceguiu para a casa {player_position[current_player]}.')
            else:
                # verifica se atingiu a casa 32, se sim imprime mensagem "parabéns".​
                print('Parabéns! Você chegou a casa final.')
        else:
            # Se a resposta estiver errada a posição diminui um, se não for a posição 0
            print('\nDesculpe! Sua resposta está incorreta. Retorne uma casa.')
            if player_position[current_player] != 0:
                player_position[current_player] -= 1
            print(f'Você voltou para a casa {player_position[current_player]}')
            wrong[players_list[current_player]] += 1

    # 3) c. solicita a resposta e verifica:​
    elif choice == 2:
        answer = int(input(f'Qual a raiz quadrada de {square}?\n\nResposta: '))
        # Se a resposta estiver correta, a posição do jogador aumenta com o número que está no dado e o algoritmo mostra a nova posição.
        if square ** 0.5 == answer:
            step_counts[players_list[current_player]] += dice
            right[players_list[current_player]] += 1
            print('\nParabéns! Você acertou a pergunta!')
            player_position[current_player] += dice
            if player_position[current_player] < 32:
                print(f'Você proceguiu para a casa {player_position[current_player]}.')
            else:
                # verifica se atingiu a casa 32, se sim imprime mensagem "parabéns".​
                print('Parabéns! Você chegou a casa final.')
        else:
            # Se a resposta estiver errada a posição diminui um, se não for a posição 0
            print('\nDesculpe! Sua resposta está incorreta. Retorne uma casa.')
            if player_position[current_player] != 0:
                player_position[current_player] -= 1
            print(f'Você voltou para a casa {player_position[current_player]}')
            wrong[players_list[current_player]] += 1

# 1) Inicializa o tabuleiro​
if __name__ == "__main__":

    players_list = []

    step_counts = {

    }

    right = {

    }

    wrong = {

    }

    print("*********************************")
    print("Bem vindo ao jogo Casa 32")
    print("*********************************", "\n")

#  1) a. O algoritmo pede o nível de dificuldade do jogo​
    game_dif = input('Digite a dificuldade do jogo: [Fácil] [Médio] [Difícil]. \n\ndificuldade:')
    game_dif = game_dif.upper()

    while game_dif != 'FACIL' and game_dif != 'FÁCIL' and game_dif != 'MEDIO' and game_dif != 'MÉDIO' and game_dif != 'DIFICIL' and game_dif != 'DIFÍCIL':
        print('\nValor inválido. Por Favor digite [Fácil] ou [Médio] ou [Difícil].')
        game_dif = input('Digite a dificuldade do jogo: [Fácil] [Médio] [Difícil]. \n\n')
        game_dif = game_dif.upper()

    num_players = 2
    player_position = [0] * num_players

#  1) b. O algoritmo pede o nome dos dois jogadores
#  1) c. A ordem dos jogadores é estabelecida conforme a ordem do cadastro dos jogadores
    print('')
    for i in range(num_players):
        player_name = input(f'Digite o nome do jogador {i + 1}: ')
        players_list.append(player_name)

    __game__()