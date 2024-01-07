use std::mem;

fn analyze_slice(slice: &[i32]) {
    println!("first element: {}", slice[0]);
    println!("the slice has {} elements.", slice.len());
}

fn main() {
    // fixes-size array
    let xs: [i32; 5] = [1, 2, 3, 4, 5];
    println!("array: {:?}", xs);

    // zeros
    let ys: [i32; 10] = [0; 10];
    println!("zeros: {:?}", ys);

    // len
    println!("xs has {} elements.", xs.len());
    // indexing
    println!("first two: {}, {}", xs[0], xs[1]);
    
    // stack allocated
    println!("xs occupies {} bytes.", mem::size_of_val(&xs));

    // can be borrowed as slices
    println!("borrow the array as a slice:");
    analyze_slice(&xs);

    println!("borrow a section:");
    analyze_slice(&xs[1..4]);

    // get
    for i in 0..xs.len()+1 {
        match xs.get(i) {
            Some(val) => println!("{}: {}", i, val),
            None => println!("Slow down! {} is too far!", i),
        }
    }
}