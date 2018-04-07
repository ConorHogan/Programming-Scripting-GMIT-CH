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
```python
x = int(input("Enter number here:"))
while x != 1:
  if x % 2 == 0: 
    x = x/2
    print (x) 
  else:
    x = (x * 3) + 1
    print (x)
 ```

### Exercise_4: Project Euler Problem 5
```python
answer = 0
known = 2520

while not answer:
    known += 1
    for denominator in range(2,21):
        if known % denominator:
            break
    else:
        answer = known

print (answer)
```

### Exercise_5: Printing Iris CVS
```python
with open("iris.csv") as iris_data:

  for line in iris_data:
    print('{:1} {:1} {:1} {:1}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))
```

### Exercise_6: Factorial Function
```python
def factorial(integer):
    x = 1
    while integer >= 1:
        x = x * integer
        integer = integer - 1
    return x

print (factorial(5))
print (factorial(7))
print (factorial(10))
```

## Additional Files
