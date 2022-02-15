from fileinput import close
import random
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

def prt_used_char():
    for i in chars:
        print(i)

f = open("wordle python/wordle-allowed-guesses.txt",'r')
allowed_guesses = list(f.readlines())
f = close()
f = open("wordle python/wordle-answers-alphabetical.txt",'r')
words_list = list(f.readlines())
f = close()
chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in range(len(words_list)):
    words_list[i] = words_list[i][:-1]
    words_list[i] = words_list[i].upper()
for i in range(len(allowed_guesses)):
    allowed_guesses[i] = allowed_guesses[i][:-1]
    allowed_guesses[i] = allowed_guesses[i].upper()

target = random.choice(words_list)

while True:
    prt_used_char()
    guess = input("\nguess : ").upper()
    if (guess not in allowed_guesses) and (guess not in words_list):
        continue
    for i in range(len(guess)):
        txt = guess[i]
        if guess[i] in target:
            txt = bcolors.WARNING + guess[i] + bcolors.ENDC
            if target[i] == guess[i]:
                txt = bcolors.OKGREEN + guess[i] + bcolors.ENDC
        print(txt,end=" ")
    if guess == target:
        print("\nyou got it!!!")
        break
