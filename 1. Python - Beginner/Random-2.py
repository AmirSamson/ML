import random

lucky_number = random.randint(1,20)

fortune_number = random.randint(1,3)
fortune_text = ''

if fortune_number == 1:
    fortune_text = "Make the most of it"
if fortune_number == 2:
    fortune_text = "It may look like a bad day, but it will get better soon"
if fortune_number == 3:
    fortune_text = "Look in the mirror, you are the miracle you were wishing for"


print(f"{fortune_text}! You're lucky number is: {lucky_number}")