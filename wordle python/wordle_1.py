class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

import random
f = open('words5.txt','r')
words = list(f.readlines())[:-1]
for i in range(len(words)):
    words[i] = words[i][:-1]
    words[i] = words[i].upper()
t_word = random.choice(words)
t_word = "SLEEP"

while True:
    guess = input("\nguess : ").upper()
    if len(guess) != 5:
        continue
    for i in range(len(guess)):
        txt = guess[i]
        if guess[i] in t_word:
            txt = bcolors.WARNING + guess[i] + bcolors.ENDC
            if t_word[i] == guess[i]:
                txt = bcolors.OKGREEN + guess[i] + bcolors.ENDC
        print(txt,end=" ")
    if guess == t_word:
        print("\nyou got it!!!")
        break