a = [3, 5, 7, 9]
# use block as a second-class value
b = a.map { |x| x + 1 }
c = a.map { |x| (lambda { |y| x >= y }) }

puts c
puts c[1].call 5 # true
puts c[1].call 6 # false