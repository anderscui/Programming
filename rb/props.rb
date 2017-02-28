class Language
	attr_reader :designer
	attr_accessor :designer

	def initialize(name, designer)
		@name = name
		@designer = designer
	end

	def name
		@name
	end

	def name= name
		@name = name
	end

	def string
		@name + " is designed by " + @designer
	end
end

lan = Language.new("Python", "Guido van Rossum")
puts(lan.string)
lan.name = "Ruby"
lan.designer = "Yukihiro Matsumoto"
puts(lan.designer)