import time




def gg(ffff):
    def ff(c):
        fff = time.time()
        f = ffff(c)
        fffff  = time.time()
        print("Время выполнения:",fffff-fff)
        return f
    return ff

@gg
def t(s):
    d = 1
    for i in range(1,s+1):
        d = d * i
    return d
g = int(input())
print(t(g))
len(str(t(g)))


# def my_first_decorator(function):
#     def wrapper():
#         func = function()
#         make_up = func.upper()
#         return make_up
#     return wrapper
#
#
# @my_first_decorator
# def ct():
#     return "Привет мир"
#
# print(ct())