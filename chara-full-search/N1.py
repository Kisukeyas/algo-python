# S = input()
# c = input()

# if c in S:
#     print('Yes')
# else:
#     print('No')

# データを受け取る
S = input()
c = input()

# S の長さを取得する
N = len(S)

# 線形探索
flag = False
for i in range(N):
    if S[i] == c:
        flag = True

# 答えを出力する
if flag: print("Yes")
else: print("No") 