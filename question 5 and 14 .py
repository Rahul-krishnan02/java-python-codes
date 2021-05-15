def bubblesort(lsit1):
    number = len(lsit1)
    for i in range(number -1):
        for j in range(number - i - 1):
            if(lsit1[j] > list1[j + 1]):
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
    return (list1)
list1=[]
a = int(input("number of elements:"))
for i in range(a):
    ele = input()
    list1.append(ele)
list2 = bubblesort(list1)
print(list2)
