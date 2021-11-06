from random import randint 
n=int(input('введите количество строк:'))
m=int(input('введите количество столбцов:'))
a=[[randint(-50, 50) for _ in range (m)] for _ in range(n)]
#вывод массива
print ('Массив:')
for i in a:
    print (i)
for i in a:
    print (*sorted(i))