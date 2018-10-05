-- func as parameters
applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)

i1 = applyTwice (+ 3) 10
s1 = applyTwice (++ " fun") "haskell is"

zipWith' :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith' _ [] _ = []
zipWith' _ _ [] = []
zipWith' f (x: xs) (y: ys) = f x y : zipWith' f xs ys

l1 = zipWith' (+) [1, 2, 3] [4, 5, 6]

flip' :: (a -> b -> c) -> (b -> a -> c)
flip' f y x = f x y

-- map
l2 = map (*2) [1..5]
l2_2 = [x*2 | x <- [1..5]]

-- filter
l3 = filter (>3) [1, 5, 2, 3, 6]
l3_2 = [x | x <- [1, 5, 2, 3, 6], x > 3]

l4 = filter (<15) (filter even [1..20])
l4_2 = [x | x <- [1..20], x < 15, even x]

--
largest :: Integer
largest = head (filter p [100000,99999..])
    where p x = x `mod` 3829 == 0

--
sumOfOddSquares = sum (takeWhile (<10000) (filter odd (map (^2) [1..])))

-- Collatz seq
collatz :: Int -> [Int]
collatz x
    | x < 1 = error "invalid input"
    | x == 1 = [1]
    | even x = x : collatz (x `div` 2)
    | otherwise = x : collatz (x*3 + 1)

-- partial map
listOfFuns = map (*) [0..]
i2 = (listOfFuns !! 4) 5

-- lambda
flip2 :: (a -> b -> c) -> b -> a -> c
flip2 f = \x y -> f y x

-- foldl

sum' :: (Num a) => [a] -> a
-- sum' xs = foldl (+) 0 xs
sum' = foldl (+) 0

map' :: (a -> b) -> [a] -> [b]
map' f xs = foldr (\x acc -> f x : acc) [] xs
l5 = map' (*3) [1..5]

-- foldr with infinite list
and' :: [Bool] -> Bool
and' xs = foldr (&&) True xs


-- $
l6 = sum (filter (> 10) (map (*2) [2..10]))
l6_2 = sum $ filter (> 10) $ map (*2) [2..10]

l7 = map ($ 3) [(4+), (10*), (^2), sqrt]

-- .

l8 = map (negate . sum . tail) [[1..5], [3..6], [1..7]]
f1 = sum . replicate 5 $ max 6.7 8.9

fn = ceiling . negate . tan . cos . max 10
