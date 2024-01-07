fn main() {
    let outer_var = 42;

    // can't capture dynamic environment in a fn item
    // help: use the `|| { ... }` closure form instead
    // fn func(i: i32) -> i32 { i + outer_var }

    // closures are anonymous
    let closure_annotated = |i: i32| -> i32 { i + outer_var };
    let closure_inferred = |i| i + outer_var;

    println!("annotated: {}", closure_annotated(1));
    println!("inferred: {}", closure_inferred(1));

    // take no args
    let one = || 1;
    println!("getting one: {}", one());
}