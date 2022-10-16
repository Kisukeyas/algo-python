# データを受け取る
N = int(input())
# 数値の全探索
M = N+1

for i in range(1,M):
    if i % 3 == 0:
        if i % 5 == 0:
            print('FizzBuzz')
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)