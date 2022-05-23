# matplotlib 패키지의 pyplot함수를 plt라는 이름으로 사용
import matplotlib.pyplot as plt

# bream data
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

# smelt data
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3,
                11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7,
                10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]


# 산점도는 x, y축으로 이뤄진 자표계에 두 변수(x, y)의 관계를 표현하는 방법이다
# scatter()는 산점도를 그리는 함수이다. 인수로 x축, y축의 값을 받는다
plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)
plt.xlabel('length')    # x축 이름
plt.ylabel('weight')    # y축 이름
plt.show()    # 그래프를 화면에 출력 => 이 결과의 그래프는 일직선에 가까운 형태로 나타나는데 이것을 "선형"적이다라고 말한다.


# k-Nearest Neighbors 알고리즘을 사용하기 위해서 2개의 데이터를 하나로 합친다
length = bream_length + smelt_length
weight = bream_weight + smelt_weight

# scilit-learn 머신러닝 패키지를 사용하려면 2차원 리스트를 만들어야한다. => [[],[],...]
fish_data = [[l, w] for l, w in zip(length, weight)]  # reference: help/zip.py
print(fish_data)
