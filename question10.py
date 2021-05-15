a = input("enter time one in mm:ss:msms ")
b = input("enter time two in mm:ss:msms ")
c = input("enter time three in mm:ss:msms ")
min1 = int(a[0:2])
min2 = int(b[0:2])
min3 = int(c[0:2])

sec1 = int(a[2:4])
sec2 = int(b[2:4])
sec3 = int(c[2:4])

ms1 = int(a[4:6])
ms2 = int(b[4:6])
ms3 = int(c[4:6])

time1 = (min1*60) + (sec1) + (ms1*1000)
time2 = (min2*60) + (sec2) + (ms2*1000)
time3 = (min3*60) + (sec3) + (ms3*1000)

mintime= min(min(time1,time2),time3)

if mintime == time1:
    print(a)
elif mintime == time2:
    print(b)
elif mintime == time3:
    print(c)



