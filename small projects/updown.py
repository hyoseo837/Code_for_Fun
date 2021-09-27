import random
target = random.randrange(100)

running = True
while running:
    try:
        guess = int(input('Guess what ? : '))
    except:
        continue
    if guess == target:
        print('you win!')
        break
    elif guess > target:
        print('guess smaller!')
    else:
        print('guess bigger!')

print(f'the answer was {target}')