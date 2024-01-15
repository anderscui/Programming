use std::ops::Deref;

struct MyBox<T>(T);

impl<T> MyBox<T> {
    fn new(x: T) -> MyBox<T> {
        MyBox(x)
    }
}

impl<T> Deref for MyBox<T> {
    type Target = T;

    fn deref(&self) -> &Self::Target {
        &self.0
    }
}

fn main() {
    let x = 5;
    let y = &x;
    assert_eq!(5, x);
    assert_eq!(5, *y);

    let x = MyBox::new(5);
    // *(x.deref())
    assert_eq!(5, *x);

    let s = MyBox::new(String::from("hello, world"));
    // two auto derefs
    let s1: &str = &s;
    // auto deref
    let s2: String = s.to_string();
}