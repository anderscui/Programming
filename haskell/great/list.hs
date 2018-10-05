-- Empty is like '[]', Cons is just like ':'
-- data List a = Empty | Cons a (List a) deriving (Show, Read, Eq, Ord)

-- l1 = 1 `Cons` (2 `Cons` (3 `Cons` Empty))

-- associative and precedence 
infixr 5 :-:

data List a = Empty | a :-: (List a) deriving (Show, Read, Eq, Ord)

infixr 5 ^++
(^++) :: List a -> List a -> List a
Empty ^++ ys = ys
(x :-: xs) ^++ ys = x :-: (xs ^++ ys)

l2 = 1 :-: 2 :-: 3 :-: Empty
l3 = 4 :-: 5 :-: 6 :-: Empty
l4 = 7 :-: 8 :-: 9 :-: Empty
l5 = l2 ^++ l3 ^++ l4
