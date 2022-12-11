# データを受け取る
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
# 配列 A の全探索
for x in A:
    # 配列 B の全探索
    for y in B:
       if x > y:
           count += 1

# 答えを出力する
print(count)
