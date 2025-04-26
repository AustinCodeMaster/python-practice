def factorial(num):
    result=1
    while num>1:
        result=result*num
        num=num-1
        
    return result
number=int(input("Enter a positive integer: "))

if number<0:
    print("There is no factorial for negative numbers ")
else:
    print("The Factorial of", number, "is",factorial(number))