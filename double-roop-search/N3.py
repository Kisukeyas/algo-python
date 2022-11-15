# データを受け取る
N, K = map(int, input().split())

Ans = 0

# 配列の全探索

for i in range(1, N+1):
    counter = 0
    for j in range(1, i+1):
        if i % j == 0:
            counter += 1

print(Ans)