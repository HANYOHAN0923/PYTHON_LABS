'''
똥 피하기 게임

Conditions:
1. 캐릭터는 화면 가장 아래에 위치
2. 캐릭터는 좌우로만 이동 가능
3. 똥은 화면 가장 위에서 떨어짐
4. 똥의 x좌표는 매번 랜덤으로 결정
5. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
6. 캐릭터가 똥과 충돌하면 게임 종료
7. FPS는 30 고정

Assests(pixel):
Background: 480 * 650
character: 70 * 70
poo: 70 * 70
'''

import pygame
import random

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("똥 피하기")

clock = pygame.time.Clock()


background = pygame.image.load("C:/Users/gksdy/PYTHON_LABS/pygame/assests/images/deep_blue.png")

character = pygame.image.load("C:/Users/gksdy/PYTHON_LABS/pygame/assests/images/1_character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height
character_speed = 1
character_to_x = 0


enemy = pygame.image.load("C:/Users/gksdy/PYTHON_LABS/pygame/assests/images/1_enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width-enemy_width)
enemy_y_pos = 0
enemy_speed = 15


running = True
while running:
    dt = clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
    
    character_x_pos += character_to_x*dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    enemy_y_pos += enemy_speed
    
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width-enemy_width)
    
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("Collision")
        running = False
    
    screen.blit(background, (0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    
    pygame.display.update()

pygame.time.delay(2000)

pygame.quit()