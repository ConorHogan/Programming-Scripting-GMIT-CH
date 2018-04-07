# Programming-Scripting-GMIT-CH

## Introduction 

## Programming and Scripting Problem Sets

### Exercise_1+2: Fib calculator
```python
def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Hogan"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)
```

### Exercise_3: Collatz Conjecture

### Exercise_4: Project Euler Problem 5

### Exercise_5: Printing Iris CVS

### Exercise_6: Factorial Function

## Additional Files
