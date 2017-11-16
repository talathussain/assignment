class ClassA:
	num = 10 
	def __init__(self,  num):
		self.n = 12 
print ("Class Variable",ClassA.num) 
ClassA.num= 15
print ("Class Variable Changed Here",ClassA.num)
obj = ClassA(5)    
print ("This Is an Instance Variable",obj.n)      
