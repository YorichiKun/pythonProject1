# Программа получает на вход два числа
# �
# a и
# �
# b. Если хотя бы одно из них является чётным, то составь число из 
# a десятков и
# b единиц, иначе сложи эти цифры.
a = int(input("введите число"))
b = int(input())
c = a % 2
d = b % 2
if c != 0:
    if d != 0:
        print(a + b)
    else:
        k = str(a) + str(b)
        print(k)
else:
    if d == 0:
        print(a + b)
    else:
        k = str(a) + str(b)
        print(k)