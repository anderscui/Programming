// rustc --crate-type=lib rary.rs
// ustc --crate-type=lib --crate-name=rary rary.rs

pub fn public_func() {
    println!("called rary's `public_func()`");
}

fn private_func() {
    println!("called rary's `private_func()`");
}

pub fn indirect_access() {
    print!("called rary's `indirect_access()`, that \n> ");
    private_func();
}