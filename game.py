import random
turns = ['rock', 'paper', 'scissors']

human_turn = input("Enter your turn = ")
computer_turn = random.choice(turns)

print(f'Human:{human_turn} vs. Computer:{computer_turn}')
if human_turn == computer_turn:
    print('Draw')

elif human_turn == 'rock' and computer_turn == 'scissors':
    print('human wins!')
elif human_turn == 'paper' and computer_turn == 'rock':
    print('human wins!')
elif human_turn == 'scissors' and computer_turn == 'paper':
    print('human wins!') 

else:
    print('Computer wins!')

