# 2. Write a Python Program to Check if a Number is Prime
a=int(input("Enter a given Number: "));
cnt=0;
i=1;
while i<=a:
    if a%i==0:
        cnt+=1;
    i+=1;
if cnt==2:
    print("Given number is prime");
else:
    print("Given number is not prime");
    