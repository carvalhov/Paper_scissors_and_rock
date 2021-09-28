#Papel, tesousa e pedra
import random
#Papel -> paper -> p 
#pedra -> Rock -> r
#Tesoura -> Scissors -> s
def game():
    player = input("Escolha como vai jogar, \n'p' para papel,\n's' para tesoura e \n'r' para pedra\nQual sua será sua escolha: ")
    computer = random.choice(['p', 's', 'r'])

    if player == computer:
      return "Você empatou!"

    if is_win(player, computer):
      return "Você ganhou!"
    else:
      return "Você foi derrotado :-("


def is_win(player, oponnent):
  #p > r, s > p, r > s;
    if (player == 'p' and oponnent == 'r') or \
       (player == 's' and oponnent == 'p') or \
       (player == 'r' and oponnent == 's'):
        return True  

print(game())
