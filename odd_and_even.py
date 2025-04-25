# writning a code to check if a number is odd or even
number=int(input("Enter a number: "))
# I have used modulus so as to didvie the number by 2 and if the remainder is zero it becomes even
if (number%2)==0:
# I have used f string to print out the integers to confirm wether it is odd or even
    print(f"{number} is even.")
else :
    print(f"{number} is odd.")
  