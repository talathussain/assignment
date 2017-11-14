# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

#==============================================================================#

num = int(input("Insert postive integer number = "))

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
	for i in range(1,num + 1):
		factorial = factorial*i
print("The factorial of",num,"is",factorial)



