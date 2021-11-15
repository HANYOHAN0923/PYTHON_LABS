import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen_size = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("New Game")

background = pygame.image.load("C:/Users/gksdy/PYTHON_LABS/pygame/assests/images/deep_blue.png")

character = pygame.image.load("C:/Users/gksdy/PYTHON_LABS/pygame/assests/images/1_character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

#이동할 좌표
to_x = 0
to_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
                
        if event.type == pygame.KEYUP: #키보드에서 손을 때면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    #케릭터 포지션 바꾸기
    character_x_pos += to_x
    character_y_pos += to_y
    
    #화면 밖으로 벗어날 경우 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
        
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    screen_size.blit(background, (0,0))
    screen_size.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update()
    
pygame.quit()