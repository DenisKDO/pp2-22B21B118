import pygame
import datetime
now=datetime.datetime.now()
now_s=int(now.second)
now_m=int(now.minute)
clock=pygame.time.Clock()
pygame.init()
screen=pygame.display.set_mode((700,525))
bg=pygame.image.load(r'images/bg.png').convert_alpha()
s=pygame.image.load(r'images/bigarm1.png').convert_alpha()
m=pygame.image.load(r'images/miniarm1.png').convert_alpha()
angle_s=(-1)*now_s*6
angle_m=(-1)*now_m*6
running=True
m_true=True
while running:
    angle_m-=0.1
    angle_s-=6
    rotated_s=pygame.transform.rotate(s,angle_s)
    rotated_s_rect=rotated_s.get_rect(center=(350,262.5))
    rotated_m=pygame.transform.rotate(m,angle_m)
    rotated_m_rect=rotated_m.get_rect(center=(350,262.5))
    screen.blit(bg,(0,0))
    screen.blit(rotated_s,rotated_s_rect)
    screen.blit(rotated_m,rotated_m_rect)
    
    
    




    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
    clock.tick(1)