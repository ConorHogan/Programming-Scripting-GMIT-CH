# Programming-Scripting-GMIT-CH

## 1. Introduction 
This repository contains the code written for each of the 6 problem sets assigned in the Programming and Scripting course.
I have also inserted a copy of the code saved in each of the problem set files under the relevant headings.
This repository also contains three additional Python files that can be ignored for the purposes of grading the problem sets. Detail on these files is included in the "Additional Files" section below.

## 2. Programming and Scripting Problem Sets

Please see below for copies of the code written for each problem set. Additional notes are included where required.

### 2.1 Exercise_1+2: Fibonacci calculator
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

### 2.2 Exercise_3: Collatz Conjecture
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

### 2.3 Exercise_4: Project Euler Problem 5
This may take some time to run, but it does work.

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

### 2.4 Exercise_5: Printing Iris CSV Data as formatted columns
Please note that "iris.csv" must be downloaded in order for this code to work. 

```python
with open("iris.csv") as iris_data:

  for line in iris_data:
    print('{:1} {:1} {:1} {:1}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))
```

### 2.5 Exercise_6: Factorial Function
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

## 3. Additional Files
There are 3 additional files contained in this respository. These can be ignored for the purpose of grading the Problem sets, but feel free to take a look if you like.

### 3.1 Decimal_to_binary.py
This converts decimal numbers into binary using division. It was writting to automate a task we were given in our Computer Architecture and Technology Convergence Class. User are prompted to enter their Year of Birth and the programme will convert this number to its binary equivalent.

### 3.2 Conorfib.py
This is the code for the homework from week 1 of this course. It has been combined with Week 2's homework in section 2.1 above.

### 3.3 Livechat_v0.3.py
This was a personal project I attempted to help me at work. We have a Live Chat system and I wanted take an export of that chats over the past year and see if I could get a count of any recurring key words. I had previously tried this at work using Excel, but it couldn't handle the volume of data that there was to sift through so I attempted the task using Python instead. 

When run the programme prompts the user to enter an "Input" file containing the text of the livechat export. It also asks for a list of "Stopwords" (common words such as Hello, hi, and, but, it etc that should not be counted) and to desingate an "Output" file to write results to. 

Results get printed into a row in Excel in the format "word:count" e.g email:52 meaning the word email appeared 52 times in chats. 


