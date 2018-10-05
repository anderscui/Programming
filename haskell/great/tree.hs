data Tree a = EmptyTree | Node a (Tree a) (Tree a) deriving (Show)

singleton :: a -> Tree a
singleton x = Node x EmptyTree EmptyTree

treeInsert :: (Ord a) => a -> Tree a -> Tree a
treeInsert x EmptyTree = singleton x
treeInsert x (Node val left right)
    | x < val = Node val (treeInsert x left) right
    | x > val = Node val left (treeInsert x right)
    | x == val = Node val left right

treeElem :: (Ord a) => a -> Tree a -> Bool
treeElem x EmptyTree = False
treeElem x (Node val left right)
    | x == val = True
    | x < val = treeElem x left
    | x > val = treeElem x right

nums = [8, 6, 4, 1, 7, 3, 5]
numsTree = foldr treeInsert EmptyTree nums

b1 = 8 `treeElem` numsTree
b2 = 10 `treeElem` numsTree
