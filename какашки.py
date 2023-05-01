from random import randint

game=True
num=randint(1,100)

print("Попробуй угадать число от 1 до 100")

while game:
    guess=int(input('Ваше предположение:'))

    if guess==num:
        print('Вы угадали верно!')
        game=False
    elif guess < num:
        print(f'Ответ неверный попробый число больше чем {guess}')
    elif guess > num:
        print(f'Ответ неверный попробуй число меньше чем {guess}')
        