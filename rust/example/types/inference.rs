fn main() {
    let elem = 5u8;

    let mut vec = Vec::new();
    // at the point, the compiler just knows it's a vec of sth. (Vec<_>)

    vec.push(elem);
    // now it knows it's Vec<u8>

    println!("{:?}", vec);
}