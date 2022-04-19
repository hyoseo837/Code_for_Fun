import random
f = open('small projects\imparative.txt','r')
verbs = f.readlines()

while True:
    if input()=='q':
        break
    print(random.choice(verbs))