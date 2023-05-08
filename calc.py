from colorama import init

init()

from colorama import Fore, Back, Style

a = float(input(Fore.GREEN+"введите 1 число"+Style.RESET_ALL))
b = float(input(Fore.GREEN+"введите 2 число"+Style.RESET_ALL))
s = input(Fore.GREEN+"введите арифметическое действие"+Style.RESET_ALL)
if s == "+":
    print(a + b)
elif s == "-":
    print(a - b)
elif s == "*":
    print(a * b)
elif s == "/":
    if b == 0:
        print(Fore.RED+"действие невозможно!!!!"+Style.RESET_ALL)
    else:
        print(a / b)
elif s == "//":
    print(a // b)
elif s == "%":
    print(a % b)
elif s == "**":
    print(a ** b)
else:
    print(Fore.RED+"вы ввели неверную операцию"+Style.RESET_ALL)
