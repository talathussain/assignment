# Write a program which accepts a sequence of comma-separated numbers from console and generate a   list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

#=============================================================================================#

list_val = input("insert a comma separated values = ")
list = list_val.split(",")
Tuple = tuple(list)
print ("List result = ",list)
print ("Tuple result = ",Tuple)