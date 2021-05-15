import math
a = input("enter which process to per form")
if a == "1":
    b = int(input("enter number 1"))
    c = int(input("enter number 2"))
    d = b+c
    print(d)
elif a == "2":
    b = int(input("enter number 1"))
    c = int(input("enter number 2"))
    d = b-c
    print(d)
elif a == "3":
    b = int(input("enter number 1"))
    c = int(input("enter number 2"))
    d = b*c
    print(d)
elif a == "4":
    b = int(input("enter number 1"))
    d = math.radians(b)
    e= math.sin(d)
    print(e)
elif a == "5":
    b = int(input("enter number 1"))
    d = math.radians(b)
    e= math.cos(d)
    print(e)
elif a == "6":
    b = int(input("enter number 1"))
    d = math.radians(b)
    e= math.tan(d)
    print(e)
elif a == "7":
    b = int(input("enter number 1"))
    c  = int(input("enter power"))
    e= math.pow(b,c)
    print(e)


