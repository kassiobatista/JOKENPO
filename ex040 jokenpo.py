
from random import randint
import pygame
from time import sleep




print('\033[35mVAMOS JOGAR PEDRA PAPEL OU TESOURA\033[m')

print('-=' * 17)

print('''Escolha uma das opções:
[0] Pedra
[1] Papel
[2] Tesoura''')


jogador = int(input('\033[35mQual é a sua jogada?\033[m'))

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)


print('\033[33mJO')
sleep(1)

print('KEN')
sleep(1)

print('PÔ!!!\033[m')
sleep(1)



print('-=' * 13)

print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))

print('-=' * 13)


if computador == 0:   #Pedra


    if jogador == 0:
        print('\033[33mEMPATE\033[m')



    elif jogador == 1:
        print('\033[32mParabéns, você ganhou!\033[m')

    elif jogador == 2:
        print('\033[31mNão foi dessa vez! Você perdeu!\033[m')

    else:
        print('JOGADA INVÁLIDA!')



elif computador == 1: #Papel


    if jogador == 0:
        print('\033[31mNão foi dessa vez! Você perdeu!\033[m')

    elif jogador == 1:
        print('\033[33mEMPATE\033[m')

    elif jogador == 2:
        print('\033[32mParabéns, você ganhou!\033[m')

    else:
        print('JOGADA INVÁLIDA!')


elif computador == 2:

    if jogador == 0:
        print('\033[32mParabéns, você ganhou!\033[m')

    elif jogador == 1:
        print('\033[31mNão foi dessa vez! Você perdeu!\033[m')

    elif jogador == 2:
        print('\033[33mEMPATE\033[m')

    else:
         print('JOGADA INVÁLIDA!')






