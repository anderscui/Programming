use std::fmt::Display;

#[derive(Debug)]
struct Excerpt<'a> {
    part: &'a str,
}

fn main() {
    // `x` does not live long enough
    // let r;
    // {
    //     let x = 5;
    //     r = &x;
    // }

    // this is ok
    let x = 5;
    let r = &x;
    println!("r: {}", r);

    let s1 = String::from("abcd");
    let s2 = "xyz";
    let result = longer(s1.as_str(), s2);
    println!("the longer str: {}", result);

    // structs
    let novel = String::from("Call me Ishmael. Some years ago...");
    let sent = novel.split('.').next().expect("Could not find a '.'");
    let excerpt = Excerpt {
        part: sent,
    };
    println!("excerpt: {:?}", excerpt);

    // generics and traits

}

fn longer<'a>(s1: &'a str, s2: &'a str) -> &'a str {
    // ^ expected named lifetime parameter
    if s1.len() > s2.len() {
        s1
    } else {
        s2
    }
}

fn longer_with_announcement<'a, T>(
    x: &'a str,
    y: &'a str,
    announcement: T
) -> &'a str
where
    T: Display,
{
    println!("announcement: {}", announcement);
    if x.len() > y.len() {
        x
    } else {
        y
    }
}