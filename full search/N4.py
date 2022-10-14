# データを受け取る
A, B = map(int, input().split()) 
cnt = 0
# 数値の全探索
max = B
if A > B:
    max = A

for i in range(1,max+1):
    if (A % i == 0 and B % i == 0):
        cnt = i

# 答えを出力する
print(cnt)