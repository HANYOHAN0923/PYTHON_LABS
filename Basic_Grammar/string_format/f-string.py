from datetime import datetime

current_time = datetime.now()

print("오늘은",current_time.year,"년",current_time.month,"월",current_time.day,"일입니다")

print(f"오늘은 {current_time.year} 년 {current_time.month} 월 {current_time.day} 일입니다")

top = "TOP"
blue_jg = "jungle Blue"
mid = "MID"
red_jg = "jungle Red"
bot = "bottom"

print("----------Summoner's Rift----------")
print(f"|{top:<33}|")
print(f"|{blue_jg:<33}|")
print(f"|{mid:^33}|")
print(f"|{red_jg:>33}|")
print(f"|{bot:>33}|")
print("-----------------------------------")