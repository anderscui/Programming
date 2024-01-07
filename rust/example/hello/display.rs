use std::fmt;

#[derive(Debug)]
struct MinMax(i64, i64);

impl fmt::Display for MinMax {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.0, self.1)
    }
}

#[derive(Debug)]
struct Point2D {
    x: f64,
    y: f64,
}

impl fmt::Display for Point2D {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "x: {}, y: {}", self.x, self.y)
    }
}

#[derive(Debug)]
struct Complex {
    real: f64,
    imag: f64,
}

impl fmt::Display for Complex {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{} + {}i", self.real, self.imag)
    }
}

struct List(Vec<i32>);

impl fmt::Display for List {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let vec = &self.0;

        write!(f, "[")?;
        
        for (i, val) in vec.iter().enumerate() {
            if i != 0 { write!(f, ", ")?; }
            write!(f, "{}: {}", i, val)?;
        }

        write!(f, "]")
    }
}

fn main() {
    let minmax = MinMax(0, 14);

    println!("Compare structs:");
    println!("Display: {}", minmax);
    println!("Debug: {:?}", minmax);
    println!("Display with name: {minmax}");

    let point = Point2D { x: 1.1, y: 2.2 };

    println!("Compare points:");
    println!("Display: {}", point);
    println!("Debug: {:?}", point);

    let c = Complex { real: 3.3, imag: 7.2 };

    println!("Compare complex:");
    println!("Display: {}", c);
    println!("Debug: {:?}", c);

    let list = List(vec![1, 2, 3]);
    println!("List: {}", list);
}