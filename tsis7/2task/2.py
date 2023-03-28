import pygame
import os
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


pygame.mixer.music.load(r'sounds/hodak.mp3')
pygame.mixer.music.play()

pause_play=False
running=True
while running:
    screen.blit(forward_arrow,(400,350))
    screen.blit(back_arrow,(35,350))
    mouse=pygame.mouse.get_pos()
    if pause_play:
        screen.blit(list_play_pause[0],(218,347))
        for event in pygame.event.get():
            if play_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                pygame.mixer.music.unpause()
                pause_play=False
    if not pause_play:
        screen.blit(list_play_pause[1],(218,347))
        for event in pygame.event.get():
            if stop_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                pygame.mixer.music.pause()
                pause_play=True
    if back_arrow_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        pygame.mixer.music.rewind()

    







    pygame.display.update()
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            running=False
            pygame.quit()