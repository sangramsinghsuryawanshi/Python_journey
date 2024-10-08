# 3. Write a Program to Print the Fibonacci Sequence
a1=int(input("Enter n given Number: "));
a=0;
b=1;
sum=0;
for i in range(1,a1+1):
    print(a);
    sum=a+b;
    a=b;
    b=sum;
    