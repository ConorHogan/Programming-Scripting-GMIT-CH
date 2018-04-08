#Exercise 1 + 2 
#Comment 1: My name is Conor, so the first and last letter of my name (C + R= 3 + 18) give the number  21. The 21st Fibonacci number is 10,946. 

#Comment 2:

#My surname is Conor
#The first letter H is number 72
#The last letter n is number 110
#Fibonacci number 182 is 48558529144435440119720805669229197641
#Ord() is a built in function in Python that returns the ASCII code for a charecter.

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
