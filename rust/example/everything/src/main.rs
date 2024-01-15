fn main() {
    let mut s = String::from("hello world");
    // string slice: &str
    // let hello = &s[0..5];
    // let world = &s[6..11];

    let word = first_word(&s);
    s.clear();

    println!("first word is: {}", word);
}

fn first_word(s: &String) -> &str {
    &s[..1]
}
