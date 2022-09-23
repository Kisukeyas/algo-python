# データを受け取る
N = int(input())
A = list(map(int,input().split()))
B = []
Max = 1

# 線形探索
for i in range(1,10):
    cnt = 0
    for t in range(0,N):
        if i == A[t]:
            cnt += 1
    B.append(cnt)
for l in range(0,9):
    if Max < B[l]:
        Max = B[l]
        Answer = B.index(B[l])+1

# 答えを出力する
print(Answer)