fn main() {
    let logical: bool = true;
    
    let a_float: f64 = 1.0;  // regular anno
    let an_int = 5i32;  // suffix anno

    let default_float = 3.0;
    let default_int = 1;  // i32

    let mut inferred_int = 12;  // infer from context
    inferred_int = 4294967296i64;

    let mut mutable = 1;
    mutable = 2;

    // overwrite with shadowning.
    let mutable = true;

    // scientific notation
    println!("1e4 is {}, -2.5e-3 is {}", 1e4, -2.5e-3);
}