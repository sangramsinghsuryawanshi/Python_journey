num1=int(input("Enter first number: "))
num2=int(input("Enter last number: "))
print(f"Prime Series from {num1} To {num2}: ")
while num1<=num2:
    cnt=0
    j=1
    while j<=num1:
        if num1%j==0:
            cnt+=1
        j+=1
    if cnt==2:
        print(num1, end=" ")
    num1+=1;
