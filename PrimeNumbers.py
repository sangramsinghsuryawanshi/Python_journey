def primeNum(num1,num2):
    i=num1
    while i<=num2:
        cnt=0
        j=1
        while j<=i:
            if i%j==0:
                cnt+=1
            j+=1
        if cnt==2:
            print(i, end=" ")
        i+=1
            
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
print("Given Prime number is: ")
primeNum(n1,n2)
