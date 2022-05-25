from re import I


flag=0
n= int(input("Enter the limit\n"))
i=1
for i in range(2,n):
    if n%i==0:
        flag=1
        
if flag==0:
    print("Number is prime")
else:
    print("Number is not prime")