# Found this one difficult for some reason. Couldn't get the data to print correctly.

with open("iris.csv") as iris_data:

  for line in iris_data:
    line_as_string = line.split(",")
    string = str(line_as_string)
    print(string[0])
