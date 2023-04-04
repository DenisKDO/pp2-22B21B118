#IMPORTS
import pygame, random, sys, time
    

#FPS
FPS=pygame.time.Clock()

pygame.init()

#SETTINGS OF DISPLAY
pygame.display.set_caption('race')
pygame.display.set_icon(pygame.image.load(r'images/racing-flag.png'))
screen=pygame.display.set_mode((500,500))
bg=pygame.image.load(r'images/roadbg.png')
bg_y=0

#ADDING INCREASING OF THE SPEED
SPEED=7
INCSPEED=pygame.USEREVENT+1
pygame.time.set_timer(INCSPEED,1000)

#SCORE
score=0

#CREATING PLAYER
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(r'images/playercar.png')
        self.rect=self.image.get_rect()
        self.rect.center=(325,400)
    def movement(self):
        keyboard=pygame.key.get_pressed()
        if self.rect.right<500:
            if keyboard[pygame.K_d]:
                self.rect.move_ip(5,0)
        if self.rect.left>10:
            if keyboard[pygame.K_a]:
                self.rect.move_ip(-5,0)
    def draw(self):
        screen.blit(self.image,self.rect)

#CREATING OTHER CARS
class Enemy(pygame.sprite.Sprite):
    def __init__(self,a):
        super().__init__()
        if a==1:
            self.image=pygame.image.load(r'images/enemycar.png')
        elif a==2:
            self.image=pygame.image.load(r'images/gruzovik.png')
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(50,450),-150)
    def movement(self):
        global score
        self.rect.move_ip(0,SPEED)
        if self.rect.bottom>600:
            self.rect.center=(random.randint(50,450),0)
    def draw(self):
        screen.blit(self.image,self.rect)

#CREATING COIN CLASS
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(r'images/coin.png')
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(30,470),-150)
    def movement(self):
        self.rect.move_ip(0,5)
        if self.rect.bottom>=600:
            self.rect.center=(random.randint(30,470),-150)
    def draw(self):
        screen.blit(self.image,self.rect)

#CREATING ENEMY AND PLAYER
player=Player()
e2=Enemy(1)
e1=Enemy(2)
coin=Coin()
#CREATING SPRITES GROUP
enemies=pygame.sprite.Group()
enemies.add(e1)
enemies.add(e2)
all_sprite=pygame.sprite.Group()
all_sprite.add(e1)
all_sprite.add(e2)
all_sprite.add(player)
all_sprite.add(coin)
coins=pygame.sprite.Group()
coins.add(coin)


#FONTS
font=pygame.font.Font(r'fonts/ChangaOne-Regular.ttf',60)
font_small=pygame.font.Font(r'fonts/ChangaOne-Regular.ttf',25)
game_over=font.render('GAME OVER',True, 'white')

pygame.mixer.music.load(r'sounds/bgsound.mp3')
pygame.mixer.music.play(-1)

coin_amout=0
score_amout=0
while True:
    #MOVING OF BG
    if bg_y==500:
        bg_y=0
    bg_y+=10
    screen.blit(bg,(0,bg_y-500))
    screen.blit(bg,(0,bg_y))

    #OUR CLASS METHODS
    for entity in all_sprite:
        screen.blit(entity.image,entity.rect)
        entity.movement()


    for event in pygame.event.get():

        #INCREASING SPEED
        if event.type==INCSPEED:
            score_amout+=1
            SPEED+=0.5
            score+=10*score_amout

        #EXIT
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    scores=font_small.render(f'METRES: {str(score)}', True, 'white')
    screen.blit(scores,(15,13))
    coin_score=font_small.render(f'SCORE: {str(coin_amout)}',True,'white')
    screen.blit(coin_score,(370,13))
    
    if e2.rect.colliderect(e1.rect):
        e1.rect.center=(random.randint(50,450),-300)



    #COINS
    if pygame.sprite.spritecollideany(player,coins):
        pygame.mixer.Sound(r'sounds/pick.mp3').play()
        coin_amout+=1
        for entity in coins:
            entity.rect.center=(random.randint(30,470),-150)
    #GAMEOVERSCREEN
    if pygame.sprite.spritecollideany(player,enemies):
        pygame.mixer.Sound(r'sounds/crash.wav').play()
        time.sleep(0.5)
        screen.fill('black')
        screen.blit(game_over,(100,210))
        pygame.display.update()
        for entity in all_sprite:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    #SET FPS
    FPS.tick(60)
        