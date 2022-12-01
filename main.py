import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# list for img
img = [rock, paper, scissors]
word = ['rock', 'paper', 'scissors']
# player input 0-2
player = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))
# prints img based on player selection
print(f'You chose: {word[player]}')
print(img[player])

# code for computer randomisation
computer = random.randint(0,2)
print(f'Computer chose: {word[computer]}')
print(img[computer])

if player < 0 or player > 2:
    print('You typed an invalid number, you lose')
elif player == 0 and computer == 2:
    print('You Win!!')
elif computer == 0 and player == 2:
    print('You Lose.')
elif player > computer:
    print('You Win!!')
elif player < computer:
    print('You lose')
elif player == computer:
    print("It's a Draw")
    