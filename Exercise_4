#project euler problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

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
