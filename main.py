from pygame import *

window = display.set_mode((700, 500))

class GameSprite():
    def __init__(self, img, speed, x, y):
        self.img = transform.scale(image.load(img), (65, 65))
        self.rect = self.img.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
        self.move_right=False
        self.move_left=False
        self.move_up=False
        self.move_down=False
        self.direction="right"

    def reset(self): 
        window.blit(self.img, (self.rect.x, self.rect.y))

class Hero(GameSprite):
   
    def move (self):
        keys = key.get_pressed()
        if keys[K_d]:
            if self.rect.x < 640:
                self.rect.x += self.speed
        if keys[K_a]:
            if self.rect.x > 5:
                self.rect.x -= self.speed
        if keys [K_w]:
            if self.rect.y > 5:
                self.rect.y -= self.speed
        if keys[K_s]:
            if self.rect.y < 440:
                self.rect.y += self.speed
        
class Enemy(GameSprite):
    def move(self, start, end):
    
        if self.direction == "right":
            self.rect.x+=5

        if self.direction == "left":
            self.rect.x -= 5

        if self.rect.x >= end:
            self.direction = "left"
        if self.rect.x <= start:
            self.direction = "right"






        
        


mixer.init()
mixer.music.load("musik.wav")
mixer.music.play()
kick = mixer.Sound("kick.ogg")

display.set_caption("Лабіринт")
background = transform.scale(image.load("background.jpg"), (700, 500))
treasure = transform.scale(image.load('treasure.png'), (150, 100))
window.blit(background, (0, 0))

clock = time.Clock()
speed = 10
cyborg = Enemy("cyborg.png",10, 50, 120)
cyborg1 = Enemy("cyborg.png",10, 50, 120)
hero1 = Hero("hero.png",10, 50, 50)

x1 = 50
y1 = 100
x2 = 50
y2 = 200

game = True

while game:
    window.blit(background, (0, 0))
    hero1.reset()
    cyborg.reset()
    cyborg1.reset()
    hero1.move()
    cyborg.move(300, 600)
    cyborg1.move(150, 400)
    window.blit(treasure, (350,350))

    for e in event.get():
        if e.type == QUIT:
            game = False









        # if e.type == KEYDOWN:
        #     if e.key == K_1:
        #         kick.play()
        #     if e.key == K_a:
        #         cyborg.move_left = True
        #     if e.key == K_d:
        #         cyborg.move_right = True
        #     if e.key == K_w:
        #         cyborg.move_up = True   
        #     if e.key == K_s:
        #         cyborg.move_down = True    


        #     if e.key == K_LEFT:
        #         hero.move_left = True
        #     if e.key == K_RIGHT:
        #         hero.move_right = True
        #     if e.key == K_UP:
        #         hero.move_up = True   
        #     if e.key == K_DOWN:
        #         hero.move_down = True 

        # if e.type == KEYUP:

        #     if e.key == K_a:
        #         cyborg.move_left = False
        #     if e.key == K_d:
        #         cyborg.move_right = False
        #     if e.key == K_w:
        #         cyborg.move_up = False   
        #     if e.key == K_s:
        #         cyborg.move_down = False  


        #     if e.key == K_LEFT:
        #         hero.move_left = False
        #     if e.key == K_RIGHT:
        #         hero.move_right = False
        #     if e.key == K_UP:
        #         hero.move_up = False   
        #     if e.key == K_DOWN:
        #         hero.move_down = False 


    # keys_pressed = key.get_pressed()

    # if keys_pressed[K_LEFT] and x1 >5:
    #     x1 -= speed
    # if keys_pressed[K_RIGHT] and x1 <595:
    #     x1 += speed
    # if keys_pressed[K_UP] and y1 >5:
    #     y1 -= speed
    # if keys_pressed[K_DOWN] and y1 <395:
    #     y1 += speed
    # if keys_pressed[K_a] and x2 >5:
    #     x2 -= speed
    # if keys_pressed[K_d] and x2 <595:
    #     x2 += speed
    # if keys_pressed[K_w] and y2 >5:
    #     y2 -= speed
    # if keys_pressed[K_s] and y2 <395:
    #     y2 += speed
        
    clock.tick(60)
    display.update()





