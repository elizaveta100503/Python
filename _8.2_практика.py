from random import randint 
n=int(input('введите количество строк:'))
m=int(input('введите количество столбцов:'))
a=[[randint(-50, 50) for _ in range (m)] for _ in range(n)]
#вывод массива
print ('Массив:')
for i in a:
    print (i)
#поиск наименьшего значения в строке 
j = [min(a[n]) for n in range(len(a))]
print ('наименьшее значение в строке:')
print(j,  end="  ")
print("        ")
#замена четных чисел нулями, нечетных - единицей
for arr in a :
    min_z = min(arr)
    arr = [(1 if min_z % 2 else 0) if j == min_z else j for j in arr]
    print(*arr)