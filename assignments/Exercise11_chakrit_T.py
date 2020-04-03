n = int(input("press number:"))
a = int(n-1)
b = int(2)
for x in range(1):
    print(" "*a,"*")
    for y in range(a):
        print(" "*(a-1),"*"+"*"*b)
        a -= 1
        b += 2

