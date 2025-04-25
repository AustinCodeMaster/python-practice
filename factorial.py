# factorial of a number using loop which is if and else statemet
def factorial(n):
    """
    to get the factorial we know n!=n*(n-1)*(n-2)...
    so from the above equation we have n!=n*(n-1)!
    We will use a concept of recursion which is the base case and the recursive case
    return 1- stops the case
    return n * factorial(n-1) calls itself with a smaller or simpler input
    """
    if n==0 or n==1 :
        return 1# base case
    else:
        return n * factorial(n-1)#recurcive case 
print(factorial(3))