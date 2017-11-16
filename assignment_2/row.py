while True:		
	try:
		values = input("Enter The Values: Row,Column ==")
		dimensions=[int(x) for x in values.split(',')]
		rowNum=dimensions[0]
		colNum=dimensions[1]
		multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
		for row in range(rowNum):
			for col in range(colNum):
				multilist[row][col]= row*col
		print (multilist) 
		break
	except:
		print("Please Re-Enter The Value of Row And Columns")
	continue


<<<<<<< HEAD:assignment_2/row.py

=======
>>>>>>> 1ebc3808030260f5e81170dfbaba75d1a3488517:assignment_2/Row.py
