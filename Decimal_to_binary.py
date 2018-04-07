# decimal to binary converter through division - FINAL VERSION
# Converts decimal to binary through division

decimal = int(input("Insert YOB here: "))

binary_list = []

while decimal > 0:
  if decimal % 2 == 0:
    binary_list.append("0")
  elif decimal % 2 > 0:
    binary_list.append("1")
  decimal = decimal // 2

binary_number = "".join(binary_list)
print (binary_number)
