
import json

client_info = {}

def load():
    # вставь код функции load()
    global client_info
    with open("client_info.json","r",encoding="utf-8") as info:
        client_info = json.load(info)
#
def save():
    global client_info
    with open("client_info.json","w",encoding="utf-8") as info:
     	json.dump(client_info,info)
#
def show_info():
    print("Информация о счетах")
    print("----------------------------------")
    for  i in client_info["accounts"]:
        print("Имя:",i["name"])
        print("Плаёжная система:", i["system"])
        print("Номер:", i["number"])
        print("Тип:", i["type"])
        print("Баланс:", i["balance"])
        print("Cрок действия:", i["validity period"])
        print("----------------------------------")
# load()
# show_info()







def predict():
    expenses = 0
    income = 0  # доходы
    months = []  # список месяцев, в которые происходили операции

    for transaction in client_info["transactions"]:
        if transaction["type"] == "списание":
            expenses += transaction["amount"]
        if transaction["type"] == "зачисление":
            income += transaction["amount"]

        if transaction["date"] not in months:
            months.append(transaction["date"])
    print("Предполагаемые расходы в следуйщем месяце: ",expenses / len(months))
    print("Прдполагаемые доходы в следуйщем месяце: ",income / len(months))
    return expenses, incomeе





def make_transaction():
    global client_info
    print("Доступные счета:")
    i = 1
    for account in client_info["accounts"]:
        print(i, "-", account["name"], "-", account["number"])
        i += 1

    account_num = input("Введите счёт: ")

    try:
        account_num = int(account_num)
    except:
        print("Ошибка ввода. Прерываю транзакцию...")
        return

    for i in range(len(client_info["accounts"])):
        if i + 1 == account_num:
            account = client_info["accounts"][i]["number"]
            break
    else:
        print("Такого счёта не существует. Прерываю транзакцию...")
        return

    # добавь код из прошлых заданий про типы транзакций, дату и сумму
    print("Типы транзакций:")
    print("1 - списание")
    print("2 - зачисление")
    transaction_type = input("Выберите тип транзакции: ")
    amount = int(input("Введите сумму: "))
    if amount > 1:
        print("Сумма не может быть меньше 1. Прерываю транзакцию...")
        return
    if transaction_type == "1":
        client_info["accounts"][account_num-1]["balance"] -= amount
    elif transaction_type == "2":
        client_info["accounts"][account_num-1]["balance"] += amount

    print("Дата транзакции")
    year = input("Введите год: ")
    month = input("Введите месяц: ")
    #
    if int(year) > 2023 or int(month) > 12 or int(month) < 1:
        print("Неверная дата. Прерываю транзакцию...")
        return
    client_info["transactions"].append({"account": account,
                                        "type": transaction_type,
                                        "date": {"year": year, "month": month},
                                        "amount": amount
                                        })

    print(client_info['transactions'][-1])
    print("...")