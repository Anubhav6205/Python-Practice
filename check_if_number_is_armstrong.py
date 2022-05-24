
n= int(input("Enter the limit\n"))
sum=0
num=n
while n>0:
    last=n%10;
    sum+=last**3
    print("Last is " ,last**3)
    print("Sum is " ,sum)
    n/=10
    

if(num==sum):
    print("Number is armstrong")
else:
    print("Number is not armstrong")