// rustc use_lib.rs --extern rary=library.rlib

fn main() {
    rary::public_func();

    rary::indirect_access();
}