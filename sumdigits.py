def sumofdigits(num):

    num= str(abs(num))#I have used the in built abs to convert numbers to absolute values
    #
    total = 0
    """
    the for loop below is used to convert each number to a string then adds them
     example is   if numbers are num=123 the loop counts '1','2','3' one by one
     it adds then returns the total
    """
    for digit in num:
        total=total+int(digit)

    return total

number=int(input("Enter a number: "))
print("The sum of digits is: " , sumofdigits(number))