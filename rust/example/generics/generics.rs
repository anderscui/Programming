// a concrete type 
struct A;

// a concrete type
struct Single(A);

// a generic type
struct SingleGen<T>(T);

// concrete fn
fn reg_fn(_s: Single) {}

// concrete fn
fn gen_spec_t(_s: SingleGen<A>) {}

// concrete fn
fn gen_spec_i32(_s: SingleGen<i32>) {}

// generic fn
fn generic<T>(_s: SingleGen<T>) {}

fn main() {
    let _s = Single(A);

    let _char: SingleGen<char> = SingleGen('a');

    let _t = SingleGen(A);
    let _i32 = SingleGen(1);
    let _char = SingleGen('a');

    reg_fn(Single(A));
    gen_spec_t(SingleGen(A));
    gen_spec_i32(SingleGen(6));

    // explicitly
    generic::<char>(SingleGen('a'));
    // implicitly
    generic(SingleGen('c'));
}