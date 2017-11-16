print ("1 For abs()")  
print ("2 for int()")  
print ("3 for input()")
print ("4 for str()")
print ("5 for staticmethod()")
print ("6 for all()")
print ("7 for file()")
print ("8 for bool()")

while True:
	try:
		list_num = int (input("select list number = "))
		if(list_num == 1):
			print(abs.__doc__)
		elif(list_num == 2):
			print(int.__doc__)
		elif(list_num == 3):
			print(input.__doc__)
		elif(list_num == 4):
			print(staticmethod.__doc__)
		elif(list_num == 5):
			print(bool.__doc__)
		elif(list_num == 6):
			print(file.__doc__)
		elif(list_num == 7):
			print(all.__doc__)
		elif(list_num == 8):
			print(str.__doc__)
		else:
			print("Please select list Number")
		
	except:
		print ("sorry! Please select list Number")
		continue


