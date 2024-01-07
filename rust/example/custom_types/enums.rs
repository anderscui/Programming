#![allow(dead_code)]
#![allow(unused_imports)]

enum WebEvent {
    // an enum variant may either be 'unit-like'
    PageLoad,
    PageUnload,
    // like tuple structs,
    KeyPress(char),
    Paste(String),
    // or c-like structs
    Click { x: i64, y: i64 },
}

// type alias
type MyEvent = WebEvent;

fn inspect(event: WebEvent) {
    match event {
        WebEvent::PageLoad => println!("page loaded"),
        WebEvent::PageUnload => println!("page unloaded"),
        WebEvent::KeyPress(c) => println!("pressed '{}'", c),
        WebEvent::Paste(s) => println!("pressed \"{}\"", s),
        WebEvent::Click { x, y } => {
            println!("clicked at x={}, y={}", x, y);
        }
    }
}

// c-like enums
enum Number {
    Zero,
    One,
    Two,
}

enum Color {
    Red = 0xff0000,
    Green = 0x00ff00,
    Blue = 0x0000ff,
}

fn main() {
    // use `use`
    use crate::Number::{Zero, One, Two};
    use crate::Color::*;

    let load = WebEvent::PageLoad;
    let unload = WebEvent::PageUnload;
    let pressed = WebEvent::KeyPress('x');
    let pasted = MyEvent::Paste("my text".to_owned());
    let click = WebEvent::Click { x: 10, y: 20 };

    inspect(load);
    inspect(unload);
    inspect(pressed);
    inspect(pasted);
    inspect(click);

    println!("zero is {}", Zero as i32);
    println!("roses are #{:06x}", Red as i32);
}