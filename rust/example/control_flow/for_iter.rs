fn main() {
    let names = vec!["Bob", "Frank", "Ferris"];

    // iter: borrow each elem
    // the collection is available for reuse after the loop
    for name in names.iter() {
        match name {
            &"Ferris" => println!("there is a rustacean among us!"),
            _ => println!("hello {}", name),
        }
    }
    println!("names: {:?}", names);

    let names = vec!["Bob", "Frank", "Ferris"];

    // into_iter: consumes the collection
    // the collection is not available for reuse after the loop
    for name in names.into_iter() {
        match name {
            "Ferris" => println!("there is a rustacean among us!"),
            _ => println!("hello {}", name),
        }
    }
    // borrow of moved value: `names`
    // println!("names: {:?}", names);

    let mut names = vec!["Bob", "Frank", "Ferris"];

    // mutably borrow
    for name in names.iter_mut() {
        *name = match name {
            &mut "Ferris" => "There is a rustacean among us!",
            _ => "Hello",
        }
    }

    println!("names: {:?}", names);
}