
class RecursionOfFact:
    ans=1
    def factOfNum(n):
        if n>=1:
           RecursionOfFact.ans*=n
           RecursionOfFact.factOfNum(n-1)
        return RecursionOfFact.ans
p1=RecursionOfFact
print("Factorial of given number is: ",p1.factOfNum(4))
