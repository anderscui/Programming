a = Array.new(5) { |i| i * i }
a.each {|x| puts (x)}
sum = a.inject(0) { |acc, i| acc + i }
puts sum
puts a.select { |i| i % 2 == 0 }