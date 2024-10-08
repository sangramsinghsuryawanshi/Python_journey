# 5. Write a Program to Find the Factorial of a Number
num=int(input("Enter n given Number: "));
f=1;
for i in range(1,num+1):
   f*=i;
print("Factorial of ",num," is ",f);
    