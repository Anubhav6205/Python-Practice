n= int(input("Enter the limit"))
rev=0
i=0
last=0
num=n
n=int(n)
while n>0:
    rev=(rev*10)+i%10
    n=n//10
    
print(rev);