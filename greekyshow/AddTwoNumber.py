#Python program to add two numbers
def AddNumber(firstvalue,secondvalue):
    result=firstvalue+secondvalue
    return result


a=int(input("Enter a number: "))
b=int(input("Enter 2nd number: "))
res=AddNumber(a,b)
print(res)

