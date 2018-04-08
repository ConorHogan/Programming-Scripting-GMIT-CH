# Programming-Scripting-GMIT-CH

## 1. Introduction 
This repository contains the code written for each of the 6 problem sets assigned in the Programming and Scripting course.
I have also inserted a copy of the code saved in each of the problem set files under the relevant headings.

This repository also contains three additional Python filessaved in the "Additional_Files" folder that can be ignored for the purposes of grading the problem sets. Detail on these files is included in the "Additional Files" section below.

Finally, the "Images" folder contains screenshots of the programmes outputs when run. These screenshots have been included along with the related snippets of code below.

## 2. Programming and Scripting Problem Sets

Please see below for copies of the code written for each problem set and screenshots of results. Additional notes are included where required.

### 2.1. Exercise_1+2: Fibonacci calculator

#### 2.1.1. Exercise_1+2 Code
```python
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
```

#### 2.1.2. Exercise_1+2 Results Screenshot
![alt text](https://github.com/ConorHogan/Programming-Scripting-GMIT-CH/blob/master/Images/Exercise2_Results.png "Exercise_1+2 Results")

### 2.2. Exercise_3: Collatz Conjecture

#### 2.2.1. Exercise_3 Code
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
 
#### 2.2.2. Exercise_3 Results Screenshot
![alt text](https://github.com/ConorHogan/Programming-Scripting-GMIT-CH/blob/master/Images/Exercise3_results.png "Exercise_3 Results")

### 2.3. Exercise_4: Project Euler Problem 5
Please note that this may take some time to run, but it does work.

#### 2.3.1. Exercise_4 Code
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

#### 2.3.2. Exercise_4 Results Screenshot
![alt text](https://github.com/ConorHogan/Programming-Scripting-GMIT-CH/blob/master/Images/Exercise4_results.png "Exercise_4 Results")

### 2.4 Exercise_5: Printing Iris CSV Data as formatted columns
Please note that "iris.csv" must be downloaded in order for this code to work. 
Results screenshot only includes a portion of the results due to length of the data.

#### 2.4.1. Exercise_5 Code
```python
with open("iris.csv") as iris_data:

  for line in iris_data:
    print('{:1} {:1} {:1} {:1}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))
```

#### 2.4.2. Exercise_5 Results Screenshot
![alt text](https://github.com/ConorHogan/Programming-Scripting-GMIT-CH/blob/master/Images/Exercise5_Results.png "Exercise_5 Results")

### 2.5. Exercise_6: Factorial Function

#### 2.5.1. Exercise_6 Code
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

#### 2.5.2. Exercise_6 Results Screenshot
![alt text](https://github.com/ConorHogan/Programming-Scripting-GMIT-CH/blob/master/Images/Exercise6_results.png "Exercise_6 Results")

## 3. Additional Files
There are 3 additional files contained in this respository. They have been saved to the "Additional_Files" folder. These can be ignored for the purpose of grading the Problem Sets, but feel free to take a look if you like. 

### 3.1. Decimal_to_binary.py
This converts decimal numbers into binary using division. It was written to automate a task we were given in our Computer Architecture and Technology Convergence Class. The User is prompted to enter their Year of Birth and the programme will convert this number to its binary equivalent.

### 3.2. Conorfib.py
This is the code for the homework from week 1 of this course. It has been combined with Week 2's homework in section 2.1 above.

### 3.3. Livechat_v0.3.py
This was a personal project I attempted to help me at work. We have a Live Chat system and I wanted take an export of that chats over the past year and see if I could get a count of any recurring key words. I had previously tried this at work using Excel, but it couldn't handle the volume of data that there was to sift through so I attempted the task using Python instead. 

When run, the programme prompts the user to enter an "Input" file containing the text of the livechat export. It also asks for a list of "Stopwords" (common words such as Hello, hi, and, but, it etc that should not be counted) and to desingate an "Output" file to write results to. 

Results get printed into a row in Excel in the format "word:count" e.g email:52 meaning the word email appeared 52 times in chats. 


