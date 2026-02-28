def square_nums():
    a = 1
    while True:
        yield a**2
        a+=1

n = int(input())

for i, j in enumerate(square_nums()):
    if i == n:
        break
    print(j)