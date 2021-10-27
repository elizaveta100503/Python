N=10
x=[]
for i in range(N):
    print('Введите число', i, 'элемент:')
    x.append(int(input()))
print(x)
for i in reversed(range(len(x)-1)):
    if x[i] in x[i+1:]:
        x.pop(i)
print(x)