count=0
a=int(input("entr the number"))
for i in range(2,a+1):
    if a%i==0:
        count=count+1;
if count<2:
    print("prime")
else:
    print("not prime")
    
