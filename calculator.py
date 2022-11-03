def Addition(a,b):
    return a+b

def Substraction(a,b):
    return a-b

def Multipliction(a,b):
    return a*b

def Division(a,b):
    return a/b

def Floor_division(a,b):
    return a//b

def fact(n):
    if n == 0:
        res = 1
    else:
        res = (n * fact(n - 1))
    return res

def reverse_str(m):
    return m[::-1]


print("Additoin is:",Addition(10,20))
print("Substraction is:",Substraction(40,20))
print("Multipliction is:",Multipliction(10,20))
print("Division is:",Division(50,5))
print("Floor Division is:",Floor_division(50,5))
print(fact(5))
print("Reverse string is:",reverse_str("Python"))

print("fsghfhjdhjdghjdghj")