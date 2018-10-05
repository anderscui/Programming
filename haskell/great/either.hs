import qualified Data.Map as Map

data LockerState = Taken | Free deriving (Show, Eq)

type Code = String

type LockerMap = Map.Map Int (LockerState, Code)

data Either' a b = Left' a | Right' b deriving (Eq, Ord, Read, Show)

lockerLookup :: Int -> LockerMap -> Either' String Code
lockerLookup number map = 
    case Map.lookup number map of
        Nothing -> Left' $ "Locker " ++ show number ++ " doesn't exist"
        Just (state, code) -> if state /= Taken
                              then Right' code
                              else Left' $ "Locker " ++ show number ++ " is taken"

lockers :: LockerMap
lockers = Map.fromList
    [(100, (Taken, "ZD39I")),
     (101, (Free, "JAH3I"))]

r1 = lockerLookup 101 lockers
r2 = lockerLookup 100 lockers
