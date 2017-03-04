type Person = {
  age: int; 
  birthday: int*int;
  name: string; 
  gender: string
}

let author = { name="anders"; age=30; gender="Male"; birthday=(6, 11)}
// fields
let name = author.name

// pattern
let { name=n; gender=g; birthday=(day, month); age=a} = author

// fun pattern
let person_name { name=n; gender=_; birthday=_; age=_} = n

let ans = person_name author