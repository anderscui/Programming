import Data.List
-- import Data.List (nub, sort)
-- import Data.List hiding (sort)
-- import qualified Data.Map as M

numUniques :: (Eq a) => [a] -> Int
numUniques = length . nub

-- counting words

wordNums :: String -> [(String, Int)]
wordNums = map (\ws -> (head ws, length ws)) . group . sort . words
nums = wordNums "a friend in need is a friend indeed"
-- [("a",2),("friend",2),("in",1),("indeed",1),("is",1),("need",1)]

-- needle in the Haystack => same to isInfixOf func

isIn :: (Eq a) => [a] -> [a] -> Bool
needle `isIn` haystack = any (needle `isPrefixOf`) (tails haystack)

b1 = "art" `isIn` "party"
b2 = [1, 2] `isIn` [1, 3, 5]

