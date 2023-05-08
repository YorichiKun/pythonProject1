def complain():
    with open("complains.txt", "a", encoding="utf-8") as f:
        f.write("\n"+input())
        print('Ваша жалоба будет рассмотрена в скором времени.')


def suggestions():
    with open("suggestions.txt","r",encoding="utf-8") as txt_f:
    print("Предожения SkysmartBank")
    print(txt_f.read())def restaurant_data():
    restaurant = {"details": []}
    with open("restaurant.txt","r",encoding="utf-8") as nnn
    for i in nnn.read().split('***\n'):
    restaurant['details'].append({
    "administrator": kuka[0],
    "workers": kuka[1],
    "turnover": kuka[2],
    "revenue": kuka[3],
    "typs": kuka[4]})
    return restaurant