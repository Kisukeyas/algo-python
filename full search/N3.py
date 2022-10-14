# データを受け取る
N = int(input())
Ans = 'No'
cnt = 0
# 数値の全探索
for i in range(1,N+1):
    if N % i == 0:
        cnt += 1
if cnt == 2:
    Ans = 'Yes'

# 答えを出力する
print(Ans)