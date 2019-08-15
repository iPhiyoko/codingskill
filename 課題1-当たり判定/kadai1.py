# -*- coding: utf-8 -*-
print('x座標 y座標 幅 高さ:', end="")
my_info = [int(i) for i in input().split()]
print('敵の数:', end="")
enemy = int(input())
enemy_info = []
distance = []
width = []

for i in range(enemy):
    array = list(map(int, input().strip().split()))
    enemy_info.append(array)
    print(enemy_info)

for i in range(enemy):  # 自機と敵機のxとyの距離を出す
    distance_width = [abs(my_info[0] - enemy_info[i][0]),
                      abs(my_info[1] - enemy_info[i][1])]
    distance.append(distance_width)
    print(distance)

for i in range(enemy):  # 自機と敵機の幅/2を出す
    array_width = [int((my_info[2] + enemy_info[i][2]) / 2),
                   int((my_info[3] + enemy_info[i][3]) / 2)]
    width.append(array_width)
    print(width)

for i in range(enemy):
    if distance[i][0] < width[i][0] and distance[i][0] < width[i][1]:
        print("敵機{0}が当たり".format(i+1))
