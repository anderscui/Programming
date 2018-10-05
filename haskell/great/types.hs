-- every exp's type is known at compile time
-- haskell has type inference

factorial :: Integer -> Integer
factorial n = product [1..n]

circumference :: Float -> Float
circumference r = 2 * pi * r

-- type class

-- read func
l1 = read "[1, 2, 3]" :: [Int]
t1 = read "(3, 'a')" :: (Int, Char)

-- type inference
l2 = [read "True", False]
