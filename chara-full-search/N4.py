# データを受け取る
N = int(input())
S = input()
T = input()

cnt = 0

# 線形探索
for i in range(N):
    if S[i] != T[i]:
        cnt += 1

# 答えを出力する
print(cnt)
