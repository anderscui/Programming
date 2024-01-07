fn main() {
    let num = 13;

    println!("tell me more about {}", num);
    match num {
        1 => println!("one"),
        2 | 3 | 5 | 7 | 11 => println!("this is a prime"),
        13..=19 => println!("a teen"),
        _ => println!("ain't special"),
    }

    let b = true;
    let binary = match b {
        false => 0,
        true => 1,
    };
    println!("{} -> {}", b, binary);
}