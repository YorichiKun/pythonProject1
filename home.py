# d = 0
# a = int(input())
# for i in range(1,a+1):
#     d = d+(i ** i)
# print(d)


# d = 1
# a = int(input())
# for i in range(2,a+1):
#     d = d/i
# print(d)


# d = 0
# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     if i % 2 == 0:
#         d = d + i
# print(d)


# d = 0
# a = int(input())
# for i in range(a+1):
#     if i % 3 == 0:
#         d = d + i
# print(d)

# Дано натуральное число
# �
# N. Вычисли:
#
# 1 1 − 2 2 + 3 3 − 4 4 + ... + 1 1 −2 2  +3 3 −4   +...+N
# d = 0
# a = int(input())
# for i in range(1,a+1):
#     if i % 2 == 0:
#         d = d - (i ** i)
#     else:
#         d = d+(i ** i)
# print(d)

# d = 0
# a = int(input())
# for i in range(1,a+1):
#     d = (i-1) * i + d
# print(d)

# a = int(input())
# if a / 1 == a and a / a == 1 and a % 2 != 0:
#     print(1)
# else:
#     print(0)

# a = int(input())
# f = 1    # f = факториал
# s = 0
# for i in range(1,a+1):
#     f = f * i
#     s = s + f
# print(s)

# a = int(input())
# f = 1    # f = факториал
# s = 0
# for i in range(1,a+1):
#     f = f * i
#     if i % 2 == 0:
#         s -= f
#     else:
#         s = s + f
# print(s)

# a = int(input())
# b = int(input())
# d = 0
# for i in range(1,a+1):
#     d = d + i ** b
# print(d)

# items = []
# s = 0
# while s == 0:
#   items.append(input())
#   n = items.pop(-1)
#   if n == '':
#      s = 1
#   else:
#       # items.append(n)
# print(items)

# g = [
#     'погулять с друзьями',
#     'почитать новости и сцепиться с кем-нибудь в комментах',
#     'почитать книжку',
#     'рассмотреть потолок',
#     'поиграть в Brawl stars',
#     'помыть посуду',
#     'сказать родителям, что заболел',
#     'залипнуть в летсплеях по роблоксу',
# ]
# # Напиши решение тут
# print(g)
# s = 0
# while s == 0:
#     n = input()
#     if n != "":
#         n = int(n)
#         del g[n]
#     else:
#         s = 1
# print(g)

# deals = [
#     'погулять с друзьями',
#     'почитать новости и сцепиться с кем-нибудь в комментах',
#     'почитать книжку',
#     'рассмотреть потолок',
#     'поиграть в Brawl stars',
#     'помыть посуду',
#     'сказать родителям, что заболел',
#     'залипнуть в летсплеях по роблоксу',
#     'покормить кота'
# ]
# # Напиши решение ниже
# for deal in deals:
#     print("Не делать уроки, а",deal)

# deals = [
#     'погулять с друзьями',
#     'почитать новости и сцепиться с кем-нибудь в комментах',
#     'почитать книжку',
#     'рассмотреть потолок',
#     'поиграть в Brawl stars',
#     'помыть посуду',
#     'сказать родителям, что заболел',
#     'залипнуть в летсплеях по роблоксу',
#     'покормить кота'
#     ]
#
# new_deals = []
# # Напиши решение ниже
# for i in deals:
#     d = str(input(i+" сделано/не сделано ? "))
#     if d == "да":
#         print(i,': ',"сделано")
#     else:
#         print(i, ': ', "не сделано")

# a = int(input())
# g = []
# for i in range(1,2*a+1):
#     if i % 2 != 0:
#         g.append(i)
# print(g)