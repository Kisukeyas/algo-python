# データを受け取る
N, value = map(int, input().split())
data = map(int, input().split())

# 線形探索
flag = False
for d in data:
    if d == value:
        flag = True

# 答えを出力する
if flag: print("Yes")
else: print("No")