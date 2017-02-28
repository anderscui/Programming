class Point
	attr_accessor :x, :y

	def initialize(x, y)
		@x = x
		@y = y
	end

	def distFromOrigin
		Math.sqrt(@x*@x + @y*@y)
	end
end

class ColorPoint < Point
	attr_accessor :color # add color and color=

	def initialize(x, y, c="red")
		super(x, y)
		@color = c
	end
end

class ThreeDPoint < Point
	attr_accessor :z

	def initialize(x, y, z)
		super(x, y)
		@z = z
	end
	def distFromOrigin
		d = super
		Math.sqrt(d*d + @z*@z)
	end
end

p = Point.new(3, 4)
puts p
cp = ColorPoint.new(5, 12, "blue")
puts cp.class.superclass.name
puts cp.is_a? Point
puts cp.instance_of? Point