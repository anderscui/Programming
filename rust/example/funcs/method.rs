struct Point {
    x: f64,
    y: f64,
}

impl Point {
    // an `associated func`
    // doesn't need to be called with an instance
    // these funcs are generally used like ctors. (cls methods in py.)
    fn origin() -> Point {
        Point { x: 0.0, y: 0.0 }
    }

    fn new(x: f64, y: f64) -> Point {
        Point { x: x, y: y}
    }
}

struct Rect {
    p1: Point,
    p2: Point,
}

impl Rect {
    // method
    // &self -> self: &Self
    // Self is the type of the caller
    fn area(&self) -> f64 {
        let Point { x: x1, y: y1 } = self.p1;
        let Point { x: x2, y: y2 } = self.p2;

        ((x1 - x2) * (y1 - y2)).abs()
    }

    fn perimeter(&self) -> f64 {
        let Point { x: x1, y: y1 } = self.p1;
        let Point { x: x2, y: y2 } = self.p2;

        2.0 * ((x1 - x2).abs() + (y1 - y2).abs())
    }

    fn translate(&mut self, x: f64, y: f64) {
        self.p1.x += x;
        self.p2.x += x;
        
        self.p1.y += y;
        self.p2.y += y;
    }
}

struct Pair(Box<i32>, Box<i32>);

impl Pair {
    // method
    // consumes the resource of the caller object
    // self -> self: Self
    fn destroy(self) {
        let Pair(first, second) = self;
        println!("Destroying Pair({}, {})", first, second);
    }
}

fn main() {
    let rect = Rect {
        // associated funcs are called using ::
        p1: Point::origin(),
        p2: Point::new(3.0, 4.0),
    };

    // methods are called using .
    println!("perimeter: {}", rect.perimeter());
    println!("area: {}", rect.area());

    let mut square = Rect {
        p1: Point::origin(),
        p2: Point::new(1.0, 1.0),
    };

    // cannot borrow `rect` as mutable, as it is not declared as mutable
    // rect.translate(1.0, 0.0);

    square.translate(1.0, 0.0);

    let pair = Pair(Box::new(1), Box::new(2));
    pair.destroy();
}