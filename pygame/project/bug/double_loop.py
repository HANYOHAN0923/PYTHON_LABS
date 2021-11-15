balls = [1,2,3,4]
weapons = [11,22,3,44]

for ball_idx, ball_val in enumerate(balls):
    print(f"ball : {ball_val}")
    
    for weapon_idx, weapon_val in enumerate(weapons):
        print(f"weapons : {weapon_val}")
        
        if ball_val == weapon_val: #충돌 체크
            print("collision")
            break
    else: #for의 변수가 더 이상 참조할 것이 없을 때 실행
        continue
    break