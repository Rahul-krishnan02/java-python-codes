def comparision(e,f):
    c= a.lower()
    d=b.lower()
    if c==d:
        if a==b:
            print("same and in same case")
        else:
            print("same but not same case")
    else:
        print("not same")


a = input("enter first string")
b = input("enter second string")
comparision(a,b)
