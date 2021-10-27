import fractions
A=int(input('введите число А:'))
B=int(input('введите число B:'))
C=int(input('введите число C:'))
D=int(input('введите число D:'))
f_one = fractions.Fraction(A, B)
f_two = fractions.Fraction(C, D)
print('A/B=', f_one)
print('C/D=', f_two)
print('A/B-C/D=', f_one-f_two)

def f_div(f_one, f_two):
    while f_one != 0 and f_two != 0:
        if f_one >= f_two:
            f_one %= f_two
        else:
            f_two %= f_one
    return f_one or f_two 
NOD = f_div(f_one, f_two)
print(NOD)