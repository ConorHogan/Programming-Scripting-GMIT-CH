# Factorial Fucntion 8-3-18

def factorial(integer):
    x = 1
    while integer >= 1:
        x = x * integer
        integer = integer - 1
    return x

print (factorial(5))
print (factorial(7))
print (factorial(10))
