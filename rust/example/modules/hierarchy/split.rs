// look for a file named `my.rs`
// insert its contents here.
mod my;

fn function() {
    println!("called `function()`");
}

fn main() {
    my::function();
    function();
    my::indirect_access();
    my::nested::function();
}