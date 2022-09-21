N, value = map(int, input().split())
data = map(int, input().split())

# 線形探索
flag = -1
count = -1
for d in data:
    count += 1
    if d == value:
        flag = count

# 答えを出力する
print(flag)