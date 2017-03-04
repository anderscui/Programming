type ArticleCode = string
type ArticleName = string
type Price = int

type Register = (ArticleCode * (ArticleName * Price))

// registers
let reg = [("a1", ("cheese", 25));
           ("a2", ("herring", 4));
           ("a3", ("soft drink", 5))]
           
type NoPieces = int
type Item = NoPieces * ArticleCode
type Purchase = Item list

type Info = NoPieces * ArticleName * Price
type InfoSeq = Info list
type Bill = InfoSeq * Price

let rec findArticle ac = function
  | (ac', adesc)::_ when ac = ac' -> adesc
  | _::reg -> findArticle ac reg
  | _ -> failwith(ac + " is an unkown article code")
  
