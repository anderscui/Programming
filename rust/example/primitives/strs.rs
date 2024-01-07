fn main() {
    // String from a slice (&str)
    // let s: String = String::from("hello world!");
    // or use to_string
    let s: String = "hello world!".to_string();

    // &s is of `&str`
    say_hello(&s);
    say_hello(&s[..]);
    say_hello(s.as_str());
}

fn say_hello(s: &str) {
    println!("{}", s);
}