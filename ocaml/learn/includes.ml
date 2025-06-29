module A = struct
  let x = 1
  let f y = y + 1
end

module B = struct
  include A
  let z = f x
  let x = 2
end
