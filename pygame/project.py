'''
Game Name: Pang

Conditions:
1. 캐릭터는 화면 아래에 위치
2. 캐릭터는 좌우 이동만 가능
3. 큰 공 1개가 나타나서 바운스
4. 무기에 닿으면 공은 작은 크기 2개로 분할
5. 가장 작은 크기의 공은 사라짐
6. 모든 공을 없애면 게임 종료(성공)
7. 캐릭터와 공이 닿으면 게임 종료(실패)
8. 시간 제한 99초 초과 시 게임 종료
9. 게임 타이머 출력
10. FPS는 30으로 고정 (필요시 speed값을 조정)

Assets(pixel):
background: 640 * 480
stage: 640 * 50
character: 33 * 60
weapon: 20 * 430
ball : 160 * 160, 80 * 80, 40 * 40, 20 * 20
'''
import pygame
import os

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Pang")

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__) #현재 파일의 위치를 반환
image_path = os.path.join(current_path,"assets\images")

#배경 만들기
background = pygame.image.load(os.path.join(image_path,"background.png"))
#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지 높이에 캐릭터를 위치시키고, 공이 튕기는 위치를 정하기위해
#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

character_to_x = 0
character_speed = 5


weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

weapons = []
weapon_speed = 10


running = True
while running:
    dt = clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                character_to_x -= character_speed
            elif event.key == pygame.K_d:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                character_to_x = 0
    
    #게임 캐릭터 위치 정의
    character_x_pos += character_to_x
    
    #게임 캐릭터 최대 이동 위치 정의
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    #무기 위치를 위로 조정
    '''
    a = [1,2,3,4]
    result = [num * 3 for num in a if num % 2 == 0]
    result = [6,12]
    [[100, 200]] -> [[100, 변동이 생김]]
    '''
    weapons = [ [wp[0], wp[1] - weapon_speed] for wp in weapons]
    #무기 천장에 닿으면 없애기
    weapons = [ [wp[0], wp[1]] for wp in weapons if wp[1] > 0]
    
    #출력 순서대로 위에 위치함
    screen.blit(background,(0,0))
    
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    pygame.display.update()
    
pygame.quit()