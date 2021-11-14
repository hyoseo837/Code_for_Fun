import pygame
import random
import time
import threading
import matplotlib.pyplot as plt
import numpy as np
import openpyxl 

w = 1280
h = 720
n_people = 100
p_infection = 10 # 10은 10%를 의미
p_recovery = 20 
p_death = 5
term = 3 # 감염확률 계산, 데이터

pygame.init()
start = time.time()

screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("abcd")
clock = pygame.time.Clock()
background = pygame.image.load("images/background.png")
#p = pygame.image.load("images/circle.png")

class Person():
    def __init__(self, id, x, y, vx, vy):
        self.id = id
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.image = pygame.image.load("images/replace.png")
        self.image2 = pygame.image.load("images/replace2.png")
        self.image3 = pygame.image.load("images/replace3.png")
        self.image4 = pygame.image.load("images/replace4.png")
        self.status = 'normal'

    def move(self):
        if self.x < 0 or self.x >= w - 20 :
            self.vx *= -1
        if self.y < 10 or self.y >= h - 20:
            self.vy *= -1
        self.x += self.vx
        self.y += self.vy

    def display(self):  
        if self.status == 'infected':
            screen.blit(self.image2, (self.x,self.y))
        elif self.status == 'recovered':
            screen.blit(self.image3, (self.x,self.y))
        elif self.status == 'deceased':
            screen.blit(self.image4, (self.x,self.y))
            self.vx = 0
            self.vy = 0
        else:
            screen.blit(self.image, ( self.x,self.y))
           
    def collide(self):
        for i in range(self.id+1,len(people)) :
            person = people[i]
            
            if self.status in ['recovered', 'deceased'] or person.status in ['recovered', 'deceased']:
                continue
            distance = ((self.x - person.x)**2 + (self.y - person.y)**2)**(1/2)
            if distance < 20 and random.randrange(0,100) < p_infection:
                if self.status == 'infected' and person.status == 'normal':
                    person.status = 'infected'
                if self.status == 'normal' and person.status == 'infected':
                    self.status = 'infected'
                             
    def change_status(self):
        if self.status == 'infected':
            if random.randrange(0,100) < p_recovery:
                self.status = 'recovered'
            if random.randrange(0,100) < p_death:
                self.status = 'deceased'


        
    
   
people = []
for i in range(n_people):
    people.append(Person(i, random.randrange(0, w-20) , random.randrange(0, h-20) ,
    random.random()*5-2.5,  random.random()*5-2.5))
    
people[0].status = 'infected'
 
def draw():
    board = {
      'normal' : 0,
      'recovered' : 0,
      'deceased' : 0,
      'infected' : 0
      }
    for person in people:
        person.move()
        person.display()
        person.collide()

        board[person.status] += 1

    for i, (status, n) in enumerate(board.items()):
        myFont = pygame.font.Font( None, 30)
        BLACK = ( 0, 0, 0 )
        text_Title= myFont.render("%s: %d" %(status, n), True, BLACK)
        screen.blit(text_Title, [5, 25 * (i + 0.5)])

                        
data_n=[]
data_r=[]
data_d=[]
data_i=[]
def TaskA():
    data_board = {
      'normal' : 0,
      'recovered' : 0,
      'deceased' : 0,
      'infected' : 0
      }
    for person in people:
        person.change_status()
        data_board[person.status] += 1
    data_n.append(data_board.get('normal'))
    data_r.append(data_board.get('recovered'))
    data_d.append(data_board.get('deceased'))
    data_i.append(data_board.get('infected'))
    
    timer = threading.Timer(term,TaskA)
    timer.start()

    if data_n[-1] == data_n[len(data_n)-2] and len(data_n) >= 10:
        timer.cancel()
    
TaskA()

running = True
while running:
    dt = clock.tick(30)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
    #screen.fill((0,0,0))
    screen.blit(background, (0,0)) #배경 그리기
   # screen.blit(p, (Random_w,Random_h))
    draw()
    pygame.display.update() #화면 다시 그리기
    

pygame.quit()


#data_n[i ] - data_n[i + 1]

print(data_n) # 정상 :
print(data_i)
print(data_r)
print(data_d)