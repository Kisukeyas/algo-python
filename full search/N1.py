# データを受け取る
N = int(input())
cnt = 0
# 数値の全探索
for i in range(1,N+1):
    if not(i % 2 == 0 or i % 3 == 0 or i % 5 == 0):
        cnt += 1

# 答えを出力する
print(cnt)