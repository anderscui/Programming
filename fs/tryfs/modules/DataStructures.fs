module DataStructs

type 'a Stack =
  | EmptyStack
  | StackNode of 'a * 'a Stack
  
let rec getRange startNum endNum =
  if startNum > endNum then EmptyStack
  else StackNode (startNum, getRange (startNum+1) endNum)
