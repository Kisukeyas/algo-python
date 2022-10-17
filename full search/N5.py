# データを受け取る
N = int(input())
# 数値の全探索

for i in range(1,N+1):
    if (i % 5 == 0 and i % 3 == 0):
        print('FizzBuzz')    
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)