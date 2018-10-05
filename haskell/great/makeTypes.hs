import Data.Map

-- record syntax

data Person = Person { firstName :: String
                     , lastName :: String
                     , age :: Int
                     , height :: Float
                     , phone :: String
                     , flavor :: String } deriving (Show)

data Car = Car { company :: String
               , model :: String
               , year :: Int
               } deriving (Show, Read, Eq)

c1 = Car "Ford" "Mustang" 1967
c2 = Car { model="Mustang", company="Ford", year=1967 }

carStr = "Car {company = \"Ford\", model = \"Mustang\", year = 1967}"
c3 = read carStr :: Car

-- type parameters

data Option a = None | Some a
o1 = None
o2 = Some 'a'

-- vector

data Vector a = Vector a a a deriving (Show)

vplus :: (Num a) => Vector a -> Vector a -> Vector a
(Vector i j k) `vplus` (Vector l m n) = Vector (i+l) (j+m) (k+n)

dot ::  (Num a) => Vector a -> Vector a -> a
(Vector i j k) `dot` (Vector l m n) = i*l + j*m + k*n

v1 = Vector 3 5 8 `vplus` Vector 9 2 8
v2 = Vector 3 5 8 `dot` Vector 9 2 8

-- ordering

data Bool = FalseVal | TrueVal deriving (Eq, Ord)

b1 = TrueVal `compare` FalseVal
b2 = TrueVal > FalseVal

-- enums

data Day = Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday 
    deriving (Eq, Ord, Show, Read, Bounded, Enum)

d1 = Wednesday
d2 = read "Wednesday" :: Day
b3 = d1 == d2
minDay = minBound :: Day
maxDay = maxBound :: Day

d4 = succ Monday
d5 = pred Wednesday
b4 = d4 == d5

-- type synonym

type PhoneNumber = String
type Name = String
type PhoneBook = [(Name, PhoneNumber)]

phonebook :: PhoneBook
phonebook = 
    [("betty", "555-2938"),
     ("bonnie", "452-2928")]

-- partial ctor
type IntMap = Map Int

-- Either

data Either a b = Left a | Right b deriving (Eq, Ord, Read, Show)

