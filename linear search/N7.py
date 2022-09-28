# データを受け取る
N = int(input())
A = list(map(int,input().split()))
Max = A[0]
cnt = 0

# 線形探索
if len(A) == 1:
    N = 0
else:
    for i in range(1,N):
        cnt += 1
        if Max < A[i]:
            Max = A[i]
            N = cnt


# 答えを出力する
print(N)