A=int (input ("Введите А:"))
B=int (input ("Введите В:"))
if (A<B):
    for i in range (A, B+1):
        print (i, end=";")
elif (A>B):
    for i in range (B,A+1):
        print (i, end=";")
