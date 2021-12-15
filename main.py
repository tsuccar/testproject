
class Car:
	def __init__(self):
		self.make="BMW"
		self.model={"a":"b","c":[10,20,30]}
		self.year=1976
		self.color="Blue"
		self.cost="200,000"
	
	def update_make(self,name):
		self.make=name
	
	def update_year(self,year):
		self.year=year
	
	def update_model(self,key,value):
		self.model[key]=value
	
	def __ge__(self, obj):
		if self.year >= obj.year:
			return True
		else:
			return False
		
		
	
my_car=Car()
his_car=Car()
his_car.update_make("Toyota")
his_car.update_year(2000)
print(my_car.make)
print(my_car.year)
print(his_car.make)
print(his_car.year)

print (his_car >= my_car)