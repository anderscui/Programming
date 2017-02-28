class A
	def initialize(f=0)
		@foo = f
	end
	def m1
		@foo = 0
	end

	def m2 x
		@foo += x
	end

	def foo
		@foo
	end
end

x = A.new
y = A.new
z = x

x.m1
print x.foo
print z.foo
