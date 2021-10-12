N = int (input ("Введите количество чисел N:"))
x = 1
y = 0
s = 0
for i in range (1, N+1):
    s = x+y
    y=x
    x=s
print (s-1)
