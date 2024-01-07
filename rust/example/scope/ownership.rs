fn destroy_box(c: Box<i32>) {
    println!("destroying a box that contains {}", c);
    // c is destroyed and the memory freed
}

fn main() {
    // stack allocated
    let x = 5u32;

    // copy x into y, no resources are moved
    let y = x;

    // both values can be independently used.
    println!("x is {}, and y is {}", x, y);

    // a is a pointer to a heap allocated value
    let a = Box::new(5i32);
    println!("a contains: {}", a);

    // move a to b
    // ** resources can only have one owner
    // a and b are both pointers to the same data
    // but b now owns it.
    let b = a;

    // a can no longer access the data
    // borrow of moved value: `a`
    // println!("a contains: {}", a);

    // this func takes ownership of the heap memory from b
    destroy_box(b);

    // b can no longer access the data
    // borrow of moved value: `b`
    println!("b contains: {}", b);
}