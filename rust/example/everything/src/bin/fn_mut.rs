fn main() {
    let mut s = String::new();
    let mut update_str = |_s| s.push_str(_s);
    update_str("hello");
    println!("{:?}", s);
}