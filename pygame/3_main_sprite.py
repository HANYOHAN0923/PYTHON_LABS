import pygame

pygame.init() #필수 초기화 단계

#화면 크기 설정
screen_width = 480 #가로 스크린 크기
screen_height = 640 #세로 스크린 크기
screen_size = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("New Game") #게임 이름

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/gksdy/PYTHON_LABS/pygame/assests/images/deep_blue.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/gksdy/PYTHON_LABS/pygame/assests/images/1_character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴, rect 사각형
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) #character 가로 위치 (가로 중앙 위치)
character_y_pos = screen_height - character_height #charcter 세로 위치 (화면 가장 아래)


#필수 event loop
running = True #게임창 유지(게임 진행 여부 확인)
while running:
    for event in pygame.event.get(): #이벤트 발생 여부 확인
        if event.type == pygame.QUIT: #창을 닫을 때 (우측 상단 "X"버튼)
            running = False
    
    #모든 그리기는 좌표의 우측 하단 방면으로 그려진다!
    screen_size.blit(background, (0,0)) #background 좌표 설정 blit(백그라운드 경로 담은 변수, 백그라운드 좌표 (0,0)은 스크린 기준 좌측상단)
    screen_size.blit(character,(character_x_pos,character_y_pos)) #케릭터 그리기
    pygame.display.update() #필수! 게임화면 다시 그리기
    
#pygame 종료
pygame.quit()