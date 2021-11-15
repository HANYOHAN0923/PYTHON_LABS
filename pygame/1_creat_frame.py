import pygame

pygame.init() #필수 초기화 단계

#화면 크기 설정
screen_width = 480 #가로 스크린 크기
screen_height = 640 #세로 스크린 크기
screen_size = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("New Game") #게임 이름

#필수 event loop
running = True #게임창 유지(게임 진행 여부 확인)
while running:
    for event in pygame.event.get(): #이벤트 발생 여부 확인
        if event.type == pygame.QUIT: #창을 닫을 때 (우측 상단 "X"버튼)
            running = False

#pygame 종료
pygame.quit()