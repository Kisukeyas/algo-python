# データを受け取る
S = input()

# S の長さを取得する
N = len(S)

cnt = 0

# 線形探索
for i in range(N-1):
    if S[i] == S[i+1]:
        cnt += 1

# 答えを出力する
print(cnt)
