a=input("Enter the number:")
b=len(a)
sum=0
for i in a:
    c=pow(int(i),b)
    sum=sum+(c)
if(sum==int(a)):
    print("Number is armstrong number")
else:
    print("Number is not armstrong number")
    
    
