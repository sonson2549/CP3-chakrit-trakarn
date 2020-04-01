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
if a == 1:
    m = int(input("How many of that:"))
    h = 36*m
print("whats more?", "if more press 1 else press 0")
mm = int(input(":"))
if mm == 1:
    a = int(input("please press you produce number:"))
    if a == 2:
        m = int(input("How many of that:"))
        ww = 8*m
    print("whats more?", "if more press 1 else press 0")
    mm = int(input(":"))
    if mm == 1:
        a = int(input("please press you produce number:"))
        if a == 3:
            m = int(input("How many of that:"))
            u = 20 * m
        print("whats more?", "if more press 1 else press 0")
        mm = int(input(":"))
        if mm == 1:
            a = int(input("please press you produce number:"))
            if a == 4:
                m = int(input("How many of that:"))
                r = 200 * m
            print("whats more?", "if more press 1 else press 0")
            mm = int(input(":"))
            if mm == 1:
                a = int(input("please press you produce number:"))
                if a == 5:
                    m = int(input("How many of that:"))
                    s = 20 * m
                print("whats more?", "if more press 1 else press 0")
                mm = int(input(":"))
                if mm == 1:
                    a = int(input("please press you produce number:"))
                    if a == 6:
                        m = int(input("How many of that:"))
                        d = 65 * m
                    print("whats more?", "if more press 1 else press 0")
                    mm = int(input(":"))
                    if mm == 1:
                        a = int(input("please press you produce number:"))
                        if a == 7:
                            m = int(input("How many of that:"))
                            z = 12 * m
                        print("whats more?", "if more press 1 else press 0")
                        mm = int(input(":"))
                        if mm == 1:
                            a = int(input("please press you produce number:"))