# more efficient than array
r = 1..100
puts r.inject { |acc, elem| acc + elem }