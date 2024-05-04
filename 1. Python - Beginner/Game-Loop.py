guees = int(input('what is your guess? '))
correct_num = 5
guess_count = 0 

while guees != correct_num:
    guess_count += 1
    guees = int(input('Opps, try again. what is your guees? '))

print(f"Congrats! The right answer was {correct_num}. It took you {guess_count} guesses.")


# ---------------------------------------

guess = int(input('what is your guess? '))
correct_num = 5
guess_count = 0 

while guess != correct_num:
    guess_count += 1
    if guess < correct_num:
        guess = int(input('Wrong! you need to guess higher. What is your guees? '))
    else:
        guess = int(input('Wrong! You need to guess lower. What is your guees? '))

print(f"Congrats! The right answer was {correct_num}. It took you {guess_count} guesses.")

# ---------------------------------------
import random

print("welcome! you should guess a number between 1 and 30")
guess = int(input('what is your guess? '))
correct_num = random.randint(1,30)
guess_count = 0 

while guess != correct_num:
    guess_count += 1
    if guess < correct_num:
        guess = int(input('Wrong! you need to guess higher. What is your guees? '))
    else:
        guess = int(input('Wrong! You need to guess lower. What is your guees? '))

print(f"Congrats! The right answer was {correct_num}. It took you {guess_count} guesses.")

# ---------------------------------------
import time
import random

time.sleep(4)
print("welcome! I am going to pick a number between 1 and 30")
time.sleep(4)
print('Picking a number...')
time.sleep(4)

guess = int(input('what is your guess? '))
correct_num = random.randint(1,30)
guess_count = 0 

while guess != correct_num:
    time.sleep(1)
    guess_count += 1
    if guess < correct_num:
        guess = int(input('Wrong! you need to guess higher. What is your guees? '))
    else:
        guess = int(input('Wrong! You need to guess lower. What is your guees? '))

print(f"Congrats! The right answer was {correct_num}. It took you {guess_count} guesses.")
time.sleep(10)