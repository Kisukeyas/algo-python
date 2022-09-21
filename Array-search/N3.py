# データを受け取る
N = map(int, input().split())
data = map(int, input().split())

# 線形探索
flag = 0
for d in data:
    if d > 0:
        flag += 1

# 答えを出力する
print(flag)