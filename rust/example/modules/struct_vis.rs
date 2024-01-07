mod my {
    // public struct with public fields
    pub struct OpenBox<T> {
        pub contents: T,
    }

    pub struct ClosedBox<T> {
        contents: T,
    }

    impl<T> ClosedBox<T> {
        // public ctor
        pub fn new(contents: T) -> ClosedBox<T> {
            ClosedBox {
                contents: contents
            }
        }
    }
}

fn main() {
    let open_box = my::OpenBox { contents: "public info" };
    println!("the open box contains: {}", open_box.contents);

    // have to use ctors
    let _closed_box = my::ClosedBox::new("classified info");
}