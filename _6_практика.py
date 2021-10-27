N = 10
x=[]
for i in range(N):
    print ('Введите число', i, 'элемент:' )
    x.append(int(input()))
print (x)
for i in range(N):
    if x[i]<0 and x[i+1]<0:
        print (x[i], x[i+1])
   