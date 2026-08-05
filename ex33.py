# Miniproject: Rock-Paper-Scissors (No loop - No func)
import random


print(
'Wellcome to this exciting game\n'.center(100) +
'!!!!!!ROCK PAPER SISORS!!!!!!'
)

possible_choices = ('r', 'p', 's')   # Immutable
possible_choices_meaning = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
match_result = None

computer_choice = random.choice(possible_choices)   # Random Choice by computer

user_choice = input(
    'You are challenged to play. Computer has already choosen!\n'
    'Choose: Rock, Paper, or Scissors?? (Enter r, p or s) '
).lower()   # Important to change to lower

if user_choice not in possible_choices:
    print('Invalid input (typo)! Try again and put in one these letters: r / p / s')
    exit(0)


user_win_condition = any([
    (user_choice == possible_choices[0] and computer_choice == possible_choices[2]), # user:r,computer:s
    (user_choice == possible_choices[1] and computer_choice == possible_choices[0]), # user:p,computer:0
    (user_choice == possible_choices[2] and computer_choice == possible_choices[1]) # user:s,computer:p
])

if user_choice == computer_choice:
    match_result = 'TIE'
elif user_win_condition:
    match_result = 'USER WINS'
else:
    match_result = 'COMPUTER WINS'

print(f'User choice: {possible_choices_meaning[user_choice]}, Computer choice: {possible_choices_meaning[computer_choice]}')
print(match_result)
print('Hope to see you again :)')
