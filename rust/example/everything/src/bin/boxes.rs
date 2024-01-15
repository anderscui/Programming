fn main() {
    // on the heap
    let a = Box::new(3);
    // 由于 Drop trait，除了作用域之后被 drop
    println!("a = {}", a);

    let b = *a + 2;
    println!("b = {}", b);

    // copy data or pointer
    // a value on the stack
    let arr = [0; 1000];
    // a deep copy
    let arr1 = arr;
    println!("arr len: {:?}", arr.len());
    println!("arr1 len: {:?}", arr1.len());

    let arr = Box::new([0; 1000]);
    // a move
    let arr1 = arr;
    // println!("arr len: {:?}", arr.len());
    println!("arr1 len: {:?}", arr1.len());
}