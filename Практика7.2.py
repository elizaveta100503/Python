n=int(input('введите число n:'))
def n_div(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i, end="  ")
delutelu = (n_div(n))

