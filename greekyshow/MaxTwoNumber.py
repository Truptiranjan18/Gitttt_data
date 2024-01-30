# Maximum of two numbers in Python

def MaxNumber(number1,number2):
    if number1>number2:
        return number1
    else:
        return number2
a=int(input("Enter a number: "))
b=int(input("Enter 2nd number: "))

res=MaxNumber(a,b)
print(res)