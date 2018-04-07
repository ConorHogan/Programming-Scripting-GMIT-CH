#Please complete the following exercise this week.
#Write a Python script that reads the Iris data set in and prints the four numerical values on each row in a nice format.
#That is, on the screen should be printed the petal length, petal width, sepal length and sepal width, and these values should have the decimal places aligned, with a space between the columns.

with open("iris.csv") as iris_data:

  for line in iris_data:
    print('{:1} {:1} {:1} {:1}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))
