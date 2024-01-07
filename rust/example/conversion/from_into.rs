use std::convert::{From, Into};

#[derive(Debug)]
struct Num {
    value: i32,
}

impl From<i32> for Num {
    fn from(item: i32) -> Self {
        Num { value: item }
    }
}

// impl Into<Num> for i32 {
//     fn into(self) -> Num {
//         Num { value: self }
//     }
// }

fn main() {
    // std types
    let my_str = "hello";
    let my_string = String::from(my_str);

    let num = Num::from(30);
    println!("the number is {:?}", num);

    // let int_val = 10;
    // let num: Num = int_val.into();
    // println!("the number is {:?}", num);
}