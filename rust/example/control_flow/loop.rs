fn main() {
    let mut count = 0u32;
    println!("let's count until infinity!");

    // infinite loop
    loop {
        count += 1;
        if count == 3 {
            println!("three");
            continue;
        }

        println!("{}", count);
        if count == 5 {
            println!("OK, that's enough");
            break;
        }
    }
}