# データを受け取る
N = int(input())
A = list(map(int,input().split()))
cnt = 0

# 線形探索
for i in range(1,N):
    if A[i-1] < A[i]:
        cnt += 1

# 答えを出力する
print(cnt)