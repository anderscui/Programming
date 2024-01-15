fn main() {
    let _v1: Vec<i32> = Vec::new();

    // type inference
    let mut v2 = Vec::new();
    v2.push(1);

    let v3 = vec![1, 2, 3];
    let third = v3[2];
    println!("{}", third);

    match v3.get(2) {
        Some(third) => println!("third: {third}"),
        None => println!("third: not available"),
    }

    // iterate
    let v4 = vec![1, 2, 3];
    for i in v4 {
        println!("{i}");
    }

    let mut v5 = vec![1, 2, 3];
    for i in &mut v5 {
        *i += 10
    }
    for i in v5 {
        println!("{i}");
    }

    // more init
    // ones
    let v6 = vec![1; 3];
    let v_from = Vec::from([1, 1, 1]);
    assert_eq!(v6, v_from);

    let mut v7 = Vec::with_capacity(10);
    v7.extend([1, 2, 3]);
    println!("len: {}, capacity: {}", v7.len(), v7.capacity());
    v7.reserve(100);
    println!("len: {}, capacity: {}", v7.len(), v7.capacity());
    v7.shrink_to_fit();
    println!("len: {}, capacity: {}", v7.len(), v7.capacity());
    assert!(!v7.is_empty());

    // sort
    let mut vec = vec![1.0, 5.6, 10.3, 2.0, 15f32];
    // vec.sort_unstable();
    vec.sort_unstable_by(|a, b| a.partial_cmp(b).unwrap());
    assert_eq!(vec, vec![1.0, 2.0, 5.6, 10.3, 15f32]);
}