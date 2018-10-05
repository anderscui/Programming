-- pattern matching

-- define a func
factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n-1)

-- for tuples
-- addVectors :: (Double, Double) -> (Double, Double)  -> (Double, Double)
-- addVectors a b = (fst a + fst b, snd a + snd b) 

addVectors :: (Double, Double) -> (Double, Double)  -> (Double, Double)
addVectors (x1, y1) (x2, y2) = (x1+x2, y1+y2)

-- list and list comprehension

pairs = [(1, 3), (4, 3), (2, 4), (5, 3), (5, 6), (3,1 )]
sums = [a+b | (a, b) <- pairs]

head' :: [a] -> a
head' [] = error "empty list!"
head' (x: _) = x

-- as-patterns

firstLetter :: String -> String
firstLetter "" = "Empty string..."
firstLetter all@(c:cs) = "The first letter of " ++ all ++ " is " ++ [c]

-- guards

-- bmiTell :: Double -> String
-- bmiTell bmi
--     | bmi <= 18.5 = "You're underweight"
--     | bmi <= 25.0 = "normal"
--     | bmi <= 30.0 = "fat"
--     | otherwise = "You're a whale"


-- where 

bmiTell :: Double -> Double -> String
bmiTell weight height
    | bmi <= skinny = "You're underweight"
    | bmi <= normal = "normal"
    | bmi <= fat = "fat"
    | otherwise = "You're a whale"
    where bmi = weight / height ^ 2
          skinny = 18.5
          normal = 25.0
          fat = 30.0

-- func in where blocks

calcBmis :: [(Double, Double)] -> [Double]
calcBmis xs = [bmi w h | (w, h) <- xs]
    where bmi weight height = weight / height ^ 2


-- let

cylinder :: Double -> Double -> Double
cylinder r h = 
    let sideArea = 2 * pi * r * h
        topArea = pi * r ^ 2
    in sideArea + 2 * topArea


-- pattern matching with let
result = (let (a, b, c) = (1, 2, 3) in a + b + c) * 100

-- list comp with let

fats :: [(Double, Double)] -> [Double]
fats xs = [bmi | (w, h) <- xs, let bmi = w / h ^ 2, bmi > 25.0]

-- case

head'2 :: [a] -> a
head'2 xs = case xs of [] -> error "empty list!"
                       (x: _) -> x

describeList :: [a] -> String
describeList ls = "The list is " ++ what ls
    where what [] = "empty"
          what [x] = "a singleton list"
          what xs = "a longer list"
