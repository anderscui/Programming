// three types of structs
// tuple - named tuples
// classic C structs
// unit structs
#![allow(dead_code)]

#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

struct Unit;

struct Pair(i32, f32);

#[derive(Debug)]
struct Point {
    x: f32,
    y: f32,
}

// nested
#[derive(Debug)]
struct Rect {
    top_left: Point,
    bottom_right: Point,
}

fn rect_area(rect: Rect) -> f32 {
    let Point { x: left, y: top } = rect.top_left;
    let Point { x: right, y: bottom } = rect.bottom_right;

    (left - right).abs() * (top - bottom).abs()
}

fn main() {
    let name = String::from("Peter");
    let age = 27;
    let peter = Person { name, age };
    println!("{:?}", peter);

    let point: Point = Point { x: 10.3, y: 0.5 };
    println!("point 1: ({}, {})", point.x, point.y);

    // update syntax
    let bottom_right = Point { x: 1.3, ..point};
    println!("point 2: ({}, {})", bottom_right.x, bottom_right.y);

    // destructure
    let Point { x: left_edge, y: top_edge } = point;
    println!("{}, {}", left_edge, top_edge);

    let _rect = Rect {
        top_left: Point { x: 6.3, y: 2.5 },
        bottom_right: bottom_right,
    };
    println!("rect: {:?}", _rect);
    println!("area: {}", rect_area(_rect));

    let _unit = Unit;

    let pair = Pair(1, 2.0);
    println!("pair: {:?}, {:?}", pair.0, pair.1);

    let Pair(integer, decimal) = pair;
    println!("pair: {:?}, {:?}", integer, decimal);
}