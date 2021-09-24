Мое рещение: 
  
  n = int(input("n: "))
c=n%10
d=n//10
if c==1 and n !=11:
    print ("На лугу ", n, "корова")
elif 2<=c<=4 and d!=1:
    print ("На лугу ", n, "коровы")
else:
    print ("На лугу ", n, "коров")
