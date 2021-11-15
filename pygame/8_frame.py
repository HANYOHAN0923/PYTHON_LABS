##########################################################################################################
import pygame

#게임 초기화
pygame.init()

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

#게임 상단 타이틀 설정
pygame.display.set_caption("New Game")

#FPS
clock = pygame.time.Clock()
##########################################################################################################

#1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트, 속도 등)
background = pygame.image.load("C:/Users/gksdy/PYTHON_LABS/pygame/assests/images/deep_blue.png")

character = pygame.image.load("C:/Users/gksdy/PYTHON_LABS/pygame/assests/images/1_character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

character_speed = 1

enemy = pygame.image.load("C:/Users/gksdy/PYTHON_LABS/pygame/assests/images/1_enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2)- (enemy_height / 2)

game_font = pygame.font.Font(None, 40)

total_time = 10

start_ticks = pygame.time.get_ticks()


##########################################################################################################

running = True
while running:

    #FPS 설정
    dt = clock.tick(30)
    
    #2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    #3. 게임 케릭터 위치 정의
    character_x_pos += to_x*dt
    character_y_pos += to_y*dt
    
    #4. 경계값 정의
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
        
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    #5. rect위치 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 처리
    if character_rect.colliderect(enemy_rect):
        print("Collision")
        running = False
    
    #6. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) #enemy 그리기
    
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #ms가 단위어서 s(초)단위로 표시
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255)) #render(시간정보, True, 출력 텍스트 RGB)
    
    screen.blit(timer, (10,10))
    
    if total_time - elapsed_time <= 0:
        print("Time out")
        running = False
    
    #7. 필수적 업데이트
    pygame.display.update()

pygame.time.delay(2000)

pygame.quit()