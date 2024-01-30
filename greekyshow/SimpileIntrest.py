# Python Program for simple interest

def simpleintrest(p):
    rate=2
    perfit=p*rate/100
    return (p+perfit)
n=int(input("Enter a number: "))
res=simpleintrest(n)
print(int(res))