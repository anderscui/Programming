struct UnPrintable(i32);

// derive `fmt::Debug` impl.
#[derive(Debug)]
struct DebugPrintable(i32);

#[derive(Debug)]
struct Deep(DebugPrintable);

fn main() {
    println!("{:?} months in a year.", 12);
    println!("{1:?} {0:?} is the {actor:?} name.",
             "Slater",
             "Christian",
             actor="actor's");

    println!("Now {:?} will print!", DebugPrintable(3));
    println!("Now {:?} will print!", Deep(DebugPrintable(3)));

    // pretty printing
    println!("Now {:#?} will print!", Deep(DebugPrintable(3)));
}