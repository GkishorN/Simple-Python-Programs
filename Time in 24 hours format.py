time=input("Enter the time(HH:MM:SS (AM/PM)):")
t=time.split(":")
c=t[2].split(" ")
if(c[1].lower()=="pm"):
    if(int(t[0])==12):
        t[0]="12"
    else:
          a=int(t[0])
          b=a+12
          t[0]=b 
else:
    if(int(t[0])==12):
        t[0]="00"
for i in range(0,2):
    print(t[i],end=":")
print(c[0],end="")
    
    
