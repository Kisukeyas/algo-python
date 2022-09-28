# データを受け取る
N, value = map(int, input().split())
data = map(int, input().split())

# 線形探索
flag = 0
for d in data:
    if d == value:
        flag += 1

# 答えを出力する
print(flag)