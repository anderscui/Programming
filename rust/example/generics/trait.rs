struct Empty;
struct Null;

trait DoubleDrop<T> {
    fn double_drop(self, _: T);
}

impl<T, U> DoubleDrop<T> for U {
    fn double_drop(self, _: T) {}
}

fn main() {
    let emtpy = Empty;
    let null = Null;

    // deallocate emtpy and null.
    emtpy.double_drop(null);

    // use of moved value: `emtpy`
    // emtpy;
    // null;
}