use deeply::nested::func as mod_func;

fn func() {
    println!("called `func()`");
}

mod deeply {
    pub mod nested {
        pub fn func() {
            println!("called `deeply::nested::func()`");
        }
    }
}

fn main() {
    mod_func();

    // block
    {
        // shadow the `func`
        use crate::deeply::nested::func;
        func();
    }

    func();
}