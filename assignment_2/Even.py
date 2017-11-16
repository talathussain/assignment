R1 = 1000
R2 = 3000
even_number = []
for i in range(R1, R2+1):
	if (i%2==0): 
		even_number.append(str(i))

print ("Even number = ",",".join(even_number))
