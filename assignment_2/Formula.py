import math
C=50
H=30
value = []
items=[x for x in input("Enter A Value of D = ").split(',')]
for d in items:
	value.append(str(int(math.sqrt(2*C*float(d)/H))))
print ("Value of Q =",','.join(value))
