class MyParentObj(object):
	def __init__(self):
		self.__private_field = 71


class MyChildObj(MyParentObj):
	def get_private_field(self):
		return self.__private_field
		

baz = MyChildObj()
# AttributeError
#print(baz.get_private_field())

assert baz._MyParentObj__private_field == 71

print(baz.__dict__)