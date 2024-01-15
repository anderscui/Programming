fn main() {
    let x = 5;
    let y = &x;

    assert_eq!(5, x);
    assert_eq!(5, *y);

    // immutable ref
    let s1 = String::from("hello");
    // &s1: ref but not own
    let len = calc_len(&s1);
    println!("len of string: {len}");

    // mutable ref
    let mut s2 = String::from("hello");
    change(&mut s2);
}

fn change(s: &mut String) {
    s.push_str(", world");
}

fn calc_len(s: &String) -> usize {
    s.len()
}