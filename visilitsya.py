import  os
import random


clear = lambda: os.system("cls")

print("привет!Я загадал слово,твоя задача угвдать его по буквам.")
input('!!!нажми энтер чтобы продолжить!!!')
clear()
print("поехали!")

words = ['пирожок', 'чебурек', 'огурец', 'сосиска', 'котик', 'квокка', 'корабль', 'самолет', 'автомобиль', 'дирижабль']
word = random.choice(words)

letters = []
isWin = True
hp = 10

while hp > 0:
    isWin = True

    for symb in word:
        if symb in letters:
            print(symb,end=" ")
        else:
            print("*", end=" ")
            isWin = False
    print()

    if isWin:
        print("ты угодал!")
        break
    letter = input("введите букву: ")
    letters.append(letter)
    clear()
    if letter not in word:
        if letter not in letters:
            hp -= 1
            print(f"осталось попыток:{hp}")
        else:
            print("Вы уже вводили эту букву.")
if hp == 0:
    print("Ты проиграл! У тебя закончились попытки.")
