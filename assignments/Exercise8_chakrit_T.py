print("--please sign up--")
username = input("username:")
password = input("password:")
print("--please sign in--")
u = input("username:")
pa = input("password:")
if u == username and pa == password:
    print("sign in sucsessful")
else:
    print("ERROR !!!")
print("-------------------")
print("welcome to son shop")
print("you can choose any produce in my shop")
print("this my produce")
print("1,apple:36 bath")
print("2,banana:8 bath")
print("3,chocalate:20 bath")
print("4,durian:200 bath")
print("5,egg:20 bath")
print("6,fish:65 bath")
print("7,water:12 bath")
a = int(input("please press you produce number:"))
if a == 1 :
    amout = int(input("how many do you want:"))
    total = amout * 36
    print(total)
elif a == 2 :
    amout = int(input("how many do you want:"))
    total = amout * 8
    print(total)
elif a == 3 :
    amout = int(input("how many do you want:"))
    total = amout * 20
    print(total)
elif a == 4 :
    amout = int(input("how many do you want:"))
    total = amout * 200
    print(total)
elif a == 5 :
    amout = int(input("how many do you want:"))
    total = amout * 20
    print(total)
elif a == 6 :
    amout = int(input("how many do you want:"))
    total = amout * 65
    print(total)
elif a == 7 :
    amout = int(input("how many do you want:"))
    total = amout * 12
    print(total)