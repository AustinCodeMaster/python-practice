# we are going to define a function called reversestring
def reversestring(string):
    reversedstring=" " #we start by an empty string which acts as a foundation for creating the reverse string
    for char in string:
        reversedstring= char + reversedstring
    return reversedstring
userinput= input("Enter any word: ")
result=reversestring(userinput)
print("The reversed String is: ", result)
    