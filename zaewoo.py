import pygame
import random 

pygame.init()

n_people = 1
w = 640
h = 640

Random_w = random.randrange(0, w)
Random_h = random.randrange(0, h)

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
        self.image = pygame.image.load("images/circle.png")
       # self.status = 'nomal' # 'infected' # 'recovered' # 'deceased'
        
    def move(self):
        if self.x < 0 or self.x >= w:
            self.vx *= -1
        if self.y < 0 or self.y >= h:
            self.vy *= -1

        self.x += self.vx
        self.y += self.vy

    def display(self):   
        screen.blit(self.image, ( self.x,self.y))

people = []
for i in range(n_people):
    people.append(Person(i, Random_w , Random_h , random.randrange(0,5), random.randrange(0,5)))

def draw():
    for person in people:
        person.move()
        person.display()
        
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