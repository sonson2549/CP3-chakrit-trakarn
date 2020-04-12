menuList = []
priceList = []


def showBill():
    print("--- My Food ---")
    total = 0
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        total += priceList[number]
    print("total :",int(total))

while True:
    menuName = input("Enter your menu:")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("price:"))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
