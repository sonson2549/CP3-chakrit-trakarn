def login():
    username = input("Username")
    password = input("Password")
    if username == "a" and password == "k":
        showMenu()
    else:
        return False

def showMenu():
    print("---Hello----")
    print("Choose 1=Calculate Vat:")
    print("Choose 2=Calculate Price")
    menuSelect()

def menuSelect():
    choose = int(input(">>"))
    if choose == 1:
        vatCalculate(int(input()))
    elif choose == 2:
        priceCalculate()

def vatCalculate(totalPrice):
    vat = 7 / 100
    result = totalPrice + (totalPrice * vat)
    print (result)

def priceCalculate():
    price1 = int(input("First Product:"))
    price2 = int(input("Second Product:"))
    return vatCalculate(price1+price2)

print(login())