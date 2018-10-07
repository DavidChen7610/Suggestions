# coding: utf-8
"""
建议5：通过适当添加空行使代码布局更为优雅，合理

# 可以参考建议02，在编辑器中使用相应的插件，统一风格
"""
import random

guesses_made = 0

name = input('Hello! What is your name?\n')
number = random.randint(1, 20)

print('Well, {name}, I am thinking of a number between 1 and 20,'.format(name=name))

guess = 0
while guesses_made < 6:
    guess = int(input('Take a guess: '))
    guesses_made += 1

    if 1 <= guess <= 20:
        if guess < number:
            print('Your guess is too low!')
        elif guess > number:
            print('Your guess is too high!')
        elif guess == number:
            break
    else:
        # raise Exception('guess input error')
        print('guess input error')
        continue

if guess == number:
    print('Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses_made))
else:
    print('Nope. The number I was thinking of was {0}'.format(number))
