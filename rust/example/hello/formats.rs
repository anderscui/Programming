fn main() {
    // fmt::Debug: use {:?}
    // fmt::Display: use {}

    // {} is replaced by any arg
    println!("December has {} days", 31);

    // positinal args
    println!("{0}, this is {1}. {1}, this is {0}", "Alice", "Bob");

    // named args
    println!("{subject} {verb} {object}",
             object="the lazy dog",
             subject="the quick brown fox",
             verb="jumps over");
    
    // format chars
    println!("Base 10: {}", 42);
    println!("Base 2: {:b}", 42);
    println!("Base 16: {:X}", 42);

    // right-justify
    println!("{number:>5}", number=10);
    // right-justify and padding
    println!("{number:0>5}", number=10);

    // precision
    let pi = 3.14159256;
    println!("Pi is {0:.3}", pi);

    #[allow(dead_code)]
    struct Struct(i32);

    // only types that impl fmt::Display can be formatted with {}
    // println!("This struct {} won't print...", Struct(3));

    // f-strings
    let number = 1.0;
    let width = 5;
    println!("{number:>width$}");
}