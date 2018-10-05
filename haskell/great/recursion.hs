maximum' :: (Ord a) => [a] -> a
maximum' [] = error "empty list"
maximum' [x] = x
maximum' (x: xs) = max x (maximum' xs)

-- replicate
replicate' :: Int -> a -> [a]
replicate' n x
    | n <= 0 = []
    | otherwise = x : replicate' (n-1) x

take' :: Int -> [a] -> [a]
take' n _
    | n <= 0 = []
take' _ [] = []
take' n (x: xs) = x : take' (n-1) xs

-- reverse

reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x: xs) = reverse' xs ++ [x]

-- repeat - infinite seq
repeat' :: a -> [a]
repeat' x = x : repeat' x

-- zip
zip' :: [a] -> [b] -> [(a, b)]
zip' [] _ = []
zip' _ [] = []
zip' (x: xs) (y: ys) = (x, y) : zip' xs ys

-- elem: type class
elem' :: (Eq a) => a -> [a] -> Bool
elem' x [] = False
elem' x (y: ys) = x == y || elem' x ys

-- quicksort, the second pattern could be omitted.
quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort [x] = [x]
quicksort (x: xs) = 
    let smaller = [a | a <- xs, a < x]
        largerOrEqual = [a | a <- xs, a >= x]
    in (quicksort smaller) ++ [x] ++ (quicksort largerOrEqual)
