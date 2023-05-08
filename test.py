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


# def make_transaction():
#     global client_info
#     print("Доступные счета:")
#     i = 1
#     for account in client_info["accounts"]:
#         print(i, "-", account["name"], "-", account["number"])
#         i += 1
#
#     account_num = input("Введите счёт: ")
#
#     try:
#         account_num = int(account_num)
#     except:
#         print("Ошибка ввода. Прерываю транзакцию...")
#         return
#
#     for i in range(len(client_info["accounts"])):
#         if i + 1 == account_num:
#             account = client_info["accounts"][i]["number"]
#             break
#     else:
#         print("Такого счёта не существует. Прерываю транзакцию...")
#         return
#     print("Типы транзакций:")
#     print("1 - списание")
#     print("2 - зачисление")
#     transaction_type = input("Выберите тип транзакции: ")
#     if transaction_type == "1":
#         transaction_type = "списание"
#     elif transaction_type == "2":
#         transaction_type = "зачисление"
#     else:
#         print("Такого типа не существует. Прерываю транзакцию...")
#         return
#
#     print("Дата транзакции")
#     year = input("Введите год: ")
#     month = input("Введите месяц: ")
#
#     if int(year) > 2023 or int(month) > 12 or int(month) < 1:
#         print("Неверная дата. Прерываю транзакцию...")
#         return
#     new_data = {"account": account,
#     		"type": transaction_type,
#               "date": {"year":year, "month": month}}
#     print(new_data)