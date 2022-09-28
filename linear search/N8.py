# データを受け取る
N = int(input())
A = list(map(int,input().split()))
Min = A[0]

# 線形探索
for i in range(1,N):
    if Min > A[i]:
        Min = A[i]

# 答えを出力する
print(Min)