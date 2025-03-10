from pygame import *
from random import *
from time import time as timer
#font.init()

window = display.set_mode((700, 500))
display.set_caption('Pin-pong')
background = transform.scale(image.load('background.jpg'), (700, 500))
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y > 5:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y < 460:
            self.rect.y -= self.speed
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 460:
            self.rect.y += self.speed

player1 = Player('racket.png',600,180,4,40,100)
player2 = Player('racket.png',50,180,4,40,100)
ball = GameSprite('tenis_ball.png',320, 200, 3, 40, 40)
game = True
while game:
    window.blit(background,(0, 0))
    player1.reset()
    player2.reset()
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    player1.update_R()
    player2.update_L()
    display.update()
    clock.tick(60)