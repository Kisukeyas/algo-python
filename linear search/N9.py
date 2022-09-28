# データを受け取る
N = int(input())
A = list(map(int,input().split()))

# 線形探索
for i in range(1,10):
    cnt = 0
    for t in range(0,N):
        if i == A[t]:
            cnt += 1
    print(cnt)