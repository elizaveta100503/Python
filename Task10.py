N = int (input ("Введите количество чисел N:"))
K = int (input ("Введите номер числа K:"))
x = 1
y = 0
s = 0
c=0
for i in range (1, N+1):
    if i <= K:
        c = x+y
    s=x+y
    y=x
    x=s
print ((s+1) - c)
