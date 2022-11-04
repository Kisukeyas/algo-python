# データを受け取る
S = input()
T = input()

Ns = len(S)
Nt = len(T)

Ans = 'No'

cnt = 0

# 線形探索
for i in range(Ns):
    if S[i] == T[0]:
        if i <= (Ns-Nt):
            for j in range(Nt):
                if T[j] == S[i+j]:
                    cnt += 1
            if cnt == Nt:
                Ans = 'Yes'



# 答えを出力する
print(Ans)
