def palindrome(a):
    if a == a[::-1]:
        print("palindrome")

    else :
        print("not a palindrome")

a = input("enter string")
palindrome(a)
