macro_rules! say_hello {
    // `()` indicates that the macro takes no argument.
    () => {
        // // The macro will expand into the contents of this block.
        println!("hello!")
    };
}

// don't repeat yourself
// dsl
// variadic interfaces.

fn main() {
    say_hello!();
}