#![allow(unreachable_code, unused_labels)]

fn main() {
    'outer: loop {
        println!("entered the outer loop");

        'inter: loop {
            println!("entered the inner loop");

            break 'outer;
        }

        println!("this point will never be reached");
    }
    println!("exited the outer loop");
}