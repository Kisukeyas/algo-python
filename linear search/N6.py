# データを受け取る
N = int(input())
A = list(map(int,input().split()))
Max = A[0]

# 線形探索
for i in range(1,N):
    if Max < A[i]:
        Max = A[i]

# 答えを出力する
print(Max)