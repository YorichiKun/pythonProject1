# Даны два целых числа a и b, причём ≤ a≤b.
# Выведи все числа в диапазоне от a до b включительно.
# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     print(i)

# Дано натуральное число
# N. Вычисли:
# 1+2+3+...+N.
# d = 0
# a = int(input())
# for i in range(a+1):
#     d = d+(i ** i)
# print(d)
# d = 0
# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     if i % 2 == 0:
#         d = d+i
# print(d)


# d = 0
# a = int(input())
# b = int(input())
# while a > b:
#     a = a-b
#     d += 1
# print(d,"остаток",a)


# a = int(input())
# while a != 0:
#     b = a % 10
#     a = a // 10
#     print(b,end="")


# Дано целое положительное число
# N. Выведи все числа Фибоначчи до числа, большего
# N. Вывод чисел запиши через пробел.

# f1 = 1
# f2 = 1
# d = 0
# a = int(input())
# print(1,1,end=" ")
# while d <= a:
#     d = f1 + f2
#     f1 = f2
#     f2 = d
#     print(d,end=" ")

# d = 1
# n = int(input())
# x = int(input())
# for i in range(1,n+1):
#     for f in range(1,i+1)
#         d = d * f
#     x**i /


# q = [1 ,2,[3,4],[5,6]]
# print(q[-2][0])

# a =[input(),input(),input()]
# print(a[0],a[-1])

# book_phones = {
#   'Квам-Дамн': '-79899899889',
#   'Лук Скамворкер': '112',
#   'Петард Вейпер': '1',
#   'Лия Моргала': '+09998765432',
#   'Эдуард Скамворкер': '0'
# }
# i = int(input('1 — показать, 2 — добавить, 3 — изменить, 4 — удалить: '))
# if i == 1:
#   h = input()
#   if h in book_phones:
#       print(book_phones[h])
#   else:
#       print('Нет в телефонной книге')
# elif i == 2:
#   h = input()
#   e = input()
#   book_phones[h]=e
#   for key in book_phones:
#     #print(key+": ", book_phones[key])
#     print(f'{key}: {book_phones[key]}')
# elif i == 3:
#   h = input()
#   e = input()
#   book_phones[h]=e
#   for key in book_phones:
#     #print(key+": ", book_phones[key])
#     print(f'{key}: {book_phones[key]}')
# elif i == 4:
#     h = input()
#     del book_phones[h]
#     for key in book_phones:
#         # print(key+": ", book_phones[key])
#         print(f'{key}: {book_phones[key]}')
# elif i == 5:
#     for g in book_phones.keys():
#         print(g)
# elif i == 6:
#     for g in book_phones.values():
#         print(g)
# else:
#     print('Такого действия нет')
#
#
# text_string = input('Текст: ').lower() # lower() - делает все буквы строчными
# text = text_string.split(' ')
# for i in range(len(text)):
#     n = '.,!?:;'
#     for b in n:
#         text[i]=text[i].replace(b,"")
# g={}
# for word in text:
#     v = 1
#     if word in g:
#         g[word]=g[word]+1
#     else:
#         g[word]=v
# for k in g :
#     print(k,"-",g[k])
#
# def divide_nums(a,b):
#     try:
#         return float(num1) / float(num2)
#     except ValueError:
#         print("Функция деления работает только с числами.")
#         return 0
#     except ZeroDivisionError:
#         print("Нельзя делить на ноль")
#         return 0
# def sum_nums(a, b):
#     try:
#         return float(a) + float(b)
#     except ValueError:
#         print("Функция сложения работает только с числами.")
#         return 0
#
#
# def divide_nums(a, b):
#     try:
#         return float(num1) / float(num2)
#     except ValueError:
#         print("Функция деления работает только с числами.")
#         return 0
#     except ZeroDivisionError:
#         print("Нельзя делить на ноль")
#         return 0
#
#
# def v_nums(a, b):
#     try:
#         return float(a) - float(b)
#     except ValueError:
#         print("Функция сложения работает только с числами.")
#         return 0
#
# def u_nums(a, b):
#     try:
#         return float(a) * float(b)
#     except ValueError:
#         print("Функция сложения работает только с числами.")
#         return 0
#
#
# print('Выберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n10. Выход')
#
# while True:
#     choice = input('Введите номер действия: ')
#     if choice in {'1', '2', '3', '4', '10'}:
#         if choice != '10':
#             if choice == "1":
#                 a = input()
#                 b = input()
#                 print(a, "+", b,"=", sum_nums(a, b))
#             elif choice == "2":
#                 a = input()
#                 b = input()
#                 print(a, "-",b,"=", v_nums(a, b))
#             elif choice == "3":
#                 a = input()
#                 b = input()
#                 print(a, "*",b,"=", u_nums(a, b))
#             elif choice == "4":
#                 a = input()
#                 b = input()
#                 print(a, "/", b,"=", divide_nums(a, b))
#         else:
#             print('Выход из калькулятора')
#             break
#     else:
#         print('Такого действия нет.')


# import random
#
#
# def generate_password(a=6):
#     l = []
#     for i in range(a):
#         s = random.randint(1,3)
#         if s == 1:
#             l.append(random.choice("abcdefghijklmnopqrstuvwxyz"))
#         elif s == 2 :
#             l.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
#         else:
#             l.append(random.choice("0123456789"))
#     d = ""
#     for f in l:
#         d = d + f
#     return d
# print()


#

# Создай список, состоящий из
# �
# N элементов, которые указываются функцией ввода данных. Первым вводом укажи размер списка (N), далее — элементы списка. Следует найти максимальное число из данного списка.
# s = int(input())
# v = []
# for i in range(s):
#     d = int(input())
#     v.append(d)
# print(v)
# print(max(v))

# s = int(input())
# v = []
# for i in range(s):
#     d = int(input())
#     if d % 2 != 0:
#         v.append(d)
# print(min(v))

# s = int(input())
# v = []
# for i in range(s):
#     d = int(input())
#     v.append(d)
# print(sum(v)/len(v))
# f = 0
# s = int(input())
# v = []
# for i in range(s):
#     d = int(input())
#     v.append(d)
# for i in v:
#     f += v.count(i) - 1
# print(f / 2)
# a = [1,2,[3,4],[5,6]]
# print(a[3][1])
# def sum_nums(a, b):
#     try:
#         return float(a) + float(b)
#     except ValueError:
#         print("Функция сложения работает только с числами.")
#         return 0

# import random
#
#
# def get_random_list(start,end,line):
#   d = []
#   for i in range(line):
#     i = random.randint(start,end)
#     d.append(i)
#   return d
# print(get_random_list(0,10,8))

# m = input()
# a = 0
# d = 1
# for i in range(1,len(m)):
#     if abs(int(m[a]) - int(m[i])) == 1:
#         d += 1
#     a += 1
# if d == len(m):
#     print(1)
# else:
#     print(0)


# def c(a):
#     s = str(input())
#     if s == "f":
#         w = (a - 32.0) / 1.8
#         return w
#     elif s == "c":
#         w = a  * 1.8 + 32.0
#         return w
# print(c(float(input())))

# def c(a):
#     b = int(a[:-1])
#     s = a[-1]
#     if s == "f":
#         w = (b - 32.0) / 1.8
#         return w
#     elif s == "c":
#         w = b * 1.8 + 32.0
#         return w
#     else:
#         return "такого действия нет"
# print(c(input()))

# class Car:
#     def __init__(self,color,brand,speed):
#         self.color = color
#         self.brand = brand
#         self.speed = speed
#         print("Автомобиль готов!")
# d = Car("tihoocean","frontier","993")
# f = Car("gray brown crimson","mem","1000-7")
# print(d)
# print(f)

class KrolIShut:
    def __init__(self):
        print("Мы классический панк")
    def probel(self):
        print("\n")
    def durak_i_molniya(self):
        print("Грохочет гром,\n Сверкает молния в ночи,\n"
              " А на холме стоит безумец и кричит:\n"
              " «Сейчас поймаю тебя в сумку,\n "
              "И сверкать ты будешь в ней\n "
              "Мне так хочется, чтоб стала ты моей!».\n")
        self.probel()
    def kukla_kolduna(self):
        print("Темный, мрачный коридор,\n"
              " Я на цыпочках, как вор,\n"
              " Пробираюсь, чуть дыша,\n"
              " Чтобы не спугнуть \n"
              "Тех, кто спит уже давно,\n"
              " Тех, кому не все равно,\n "
              "В чью я комнату тайком Желаю заглянуть,\n"
              " Чтобы увидеть… \n")
        self.probel()

f = KrolIShut()

f.durak_i_molniya()
f.kukla_kolduna()