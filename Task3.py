A=int (input ("Введите А:"))
B=int (input ("Введите В:"))
if A>B:
    for i in range(A - (A + 1) % 2, B - B % 2, -2):
        print(i, end='; ')
else :
    print ("А не может быть меньше B по условию")