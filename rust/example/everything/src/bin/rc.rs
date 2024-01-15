use std::rc::Rc;

fn main() {
    let a = Rc::new(String::from("hello, world"));
    // clone of a pointer
    let b = Rc::clone(&a);

    assert_eq!(2, Rc::strong_count(&a));
    assert_eq!(Rc::strong_count(&a), Rc::strong_count(&b));
    {
        let c = Rc::clone(&a);
        println!("rc count after c = {}", Rc::strong_count(&a));
    }
    println!("rc count after scope of c = {}", Rc::strong_count(&a));
}