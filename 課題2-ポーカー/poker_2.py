import pprint

print('手札を入力して下さい:', end="")
games = []
num = []
suit = []
number =[]
royal = 0
for i in range(5):
    array = list(map(int, input().strip().split()))
    games.append(array)
   
    if games[i][0] == 0:
        suit.append('S')
    elif games[i][0] == 1:
        suit.append('C')
    elif games[i][0] == 2:
        suit.append('D')
    else:
        suit.append('H')
    
    if games[i][1] == 11:
        number.append('J')
        royal += 1

    elif games[i][1] == 12:
        number.append('Q')
        royal += 1
    elif games[i][1] == 13:
        number.append('K')
        royal += 1
    elif games[i][1] == 1:
        number.append('A')
        royal += 1

    else:
        number.append(games[i][1])
   
    if games[i][1] == 10:
        royal += 1
for i in range(5):
    print (suit[i], number[i], ' ', end="")

print ()

games.sort(key=lambda x: x[1], reverse=True)

S_suit = 0
C_suit = 0
D_suit = 0
H_suit = 0 
for i in range(5):
    if games[i][0] == 0:
        S_suit += 1
    elif games[i][0] == 1:
        C_suit += 1
    elif games[i][0] == 2:
        D_suit += 1
    elif games[i][0] == 3:
        H_suit += 1

    num.append(int(games[i][1]))

flag = 0
count = 0

for i in range(4):  # 連番判定
    if num[i] - num[i+1] == 1:
        count += 1 
    elif num.count(1) > 0 and num.count(13) > 0 and flag == 0:
        count += 1
        flag = 1

sn_count1 = 0

j = 0
for i in range(4):  # フルハウスとフォーカードの判定
    if num[j] - num[i+1] == 0 :
        sn_count1 += 1
    else:
        j += 1


two_p = 0
sn_count2 = 0
sn_count3 = 0

for i in range(4):  # スリーカードとツーペアの判定
    if num[i] - num[i+1] == 0 and two_p == 0:
        sn_count2 += 1
    elif num[i] - num[i+1] == 0:
        sn_count3 += 1
    elif sn_count2 > 0 and i > 0:
        two_p = 1


if S_suit == 5 or H_suit == 5 or D_suit == 5 or C_suit == 5 and royal == 5:
    print ('ロイヤルストレートフラッシュ')
elif S_suit == 5 or H_suit == 5 or D_suit == 5 or C_suit == 5 and count == 4:
    print ('ストレートフラッシュ')
elif count == 3:
    print ('フォーカード')
elif sn_count1 == 3:
    print ('フルハウス')
elif S_suit == 5 or H_suit == 5 or D_suit == 5 or C_suit == 5:
    print ('フラッシュ')
elif count == 4:
    print ('ストレート')
elif sn_count2 == 2 and sn_count3 == 0:
    print ('スリーカード')
elif sn_count2 == 1 and sn_count3 == 1:
    print ('ツーペア')
elif sn_count2 == 1:
    print ('ワンペア')
else:
    print ('ハイカード')
