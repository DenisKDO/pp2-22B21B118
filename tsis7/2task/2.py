import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption('MP3 PLAYER')
pygame.display.set_icon(pygame.image.load(r'images/mp3player/mp3-player.png').convert_alpha())
screen.fill((255,255,255))
forward_arrow=pygame.image.load(r'images/mp3player/forward.png')
forward_arrow_rect=forward_arrow.get_rect(topleft=(400,350))
list_play_pause=[
    pygame.image.load(r'images/mp3player/play.png'),
    pygame.image.load(r'images/mp3player/stop.png'),
]
back_arrow=pygame.image.load(r'images/mp3player/back.png')
back_arrow_rect=back_arrow.get_rect(topleft=(35,350))
play_button_rect=list_play_pause[0].get_rect(topleft=(218,347))
stop_button_rect=list_play_pause[1].get_rect(topleft=(218,347))

mus=[
pygame.mixer.Sound(r'sounds/hodak.mp3'),
pygame.mixer.Sound(r'sounds/taetdim.mp3'),
pygame.mixer.Sound(r'sounds/pride.mp3')
]
ch=mus[0].play()

now_mus=0

play_pause_count=1
running=True
vol=1.0
while running:
    screen.blit(forward_arrow,(400,350))
    screen.blit(back_arrow,(35,350))
    screen.blit(list_play_pause[play_pause_count],(218,347))
    mouse=pygame.mouse.get_pos()
    
    







    pygame.display.update()
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            running=False
            pygame.quit()
        elif i.type==pygame.KEYDOWN:
            if i.key==pygame.K_UP:
                vol+=0.1
                pygame.mixer.music.set_volume(vol)
            elif i.key==pygame.K_DOWN:
                vol-=0.1
                pygame.mixer.music.set_volume(vol)

        if i.type==pygame.MOUSEBUTTONDOWN:
            if forward_arrow_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and pygame.MOUSEBUTTONUP:
                if now_mus+1==len(mus):
                    continue
                else: 
                    now_mus+=1  
                    ch.stop()
                    ch=mus[now_mus].play()
                    play_pause_count=1
            elif back_arrow_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and pygame.MOUSEBUTTONUP:
                if now_mus==0:
                    continue
                else:
                    now_mus-=1
                    ch.stop()
                    ch=mus[now_mus].play()
                    play_pause_count=1

        if play_pause_count==1:
            if stop_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]: 
                ch.pause()
                play_pause_count=0
            elif i.type==pygame.KEYDOWN:
                if i.key==pygame.K_SPACE:
                    ch.pause()
                    play_pause_count=0
        elif play_pause_count==0:
            if play_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                ch.unpause()
                play_pause_count=1
            elif i.type==pygame.KEYDOWN:
                if i.key==pygame.K_SPACE:
                    ch.unpause()
                    play_pause_count=1
        