def restaurant_data():
    restaurant = {"details": []}
    with open("restaurant.txt","r",encoding="utf-8") as kukazyabra:
        for i in kukazyabra.read().split("***\n"):
            kuka = i.split("\n")
            restaurant["details"].append({
                "administrator":kuka[0],
                "workers":kuka[1],
                "turnover":kuka[2],
                "revenue":kuka[3],
                "typs":kuka[4]})
        return restaurant
print(restaurant_data())


