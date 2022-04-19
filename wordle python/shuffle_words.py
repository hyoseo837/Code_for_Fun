import random

f = open("wordle python/wordle-answers-alphabetical.txt","r")
texts = f.readlines()
f.close()

random.shuffle(texts)

f = open("wordle python\wordle-answers-shuffled.txt",'w')
f.writelines(texts)
f.close