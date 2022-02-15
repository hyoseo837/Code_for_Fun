import random
subject = ["I","You","He","She","We","You guys","They"]
verbs = ["wake up","shower","have breakfast","have lunch","have dinner","brush teeth","brush hair","brush hair","get dressed", "go school","return home","learn","do homework","shave","leave home","play soccer","go to bed","sleep","bathe","wash face","go work","go bathroom","listen music","learn","watch television","talk on the phone","get up","wash hair","get make up","read books","write"]
time = list(range(24))
minute = list(range(0,60,5))

while True:
    print(random.choice(subject) +" "+ random.choice(verbs) +" at "+ str(random.choice(time))+" : "+str(random.choice(minute)))
    print(random.choice(subject) +" "+ random.choice(verbs) +" at "+ str(random.choice(time))+" : "+str(random.choice(minute)))
    print(random.choice(subject) +" "+ random.choice(verbs) +" at "+ str(random.choice(time))+" : "+str(random.choice(minute)))
    print(random.choice(subject) +" "+ random.choice(verbs) +" at "+ str(random.choice(time))+" : "+str(random.choice(minute)))
    print(random.choice(subject) +" "+ random.choice(verbs) +" at "+ str(random.choice(time))+" : "+str(random.choice(minute)))
    if input() == "q":
        break