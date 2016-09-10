class MyObject(object):
	def __init__(self):
		self.public_field = 5
		self.__private_field = 10

	def get_private_field(self):
		return self.__private_field

	@classmethod
	def get_private_field_of_instance(cls, instance):
		return instance.__private_field


foo = MyObject()
assert foo.public_field == 5

# access private field directly
# AttributeError
#print(foo.__private_field)

# by class method
bar = MyObject()
assert MyObject.get_private_field_of_instance(bar)