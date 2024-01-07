fn main() {
    let shadowed_binding = 1;
    {
        println!("before shadowed: {}", shadowed_binding);

        let shadowed_binding = "abc";
        println!("shadowed in inner block: {}", shadowed_binding);
    }
    println!("outside inner block: {}", shadowed_binding);

    // shadows the previous binding, even the type!
    let shadowed_binding = "abc";
    println!("shadowed in outer block: {}", shadowed_binding);
}