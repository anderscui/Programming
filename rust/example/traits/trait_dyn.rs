struct Sheep {}
struct Cow {}

trait Animal {
    fn noise(&self) -> &'static str;
}

impl Animal for Sheep {
    fn noise(&self) -> &'static str {
        "baaaaah!"
    }
}

impl Animal for Cow {
    fn noise(&self) -> &'static str {
        "mooooo!"
    }
}

fn random_animal(random_num: f64) -> Box<dyn Animal> {
    if random_num < 0.5 {
        Box::new(Sheep {})
    } else {
        Box::new(Cow {})
    }
}

fn main() {
    let random_num = 0.234;
    let animal = random_animal(random_num);
    println!("You've randomly chosen an animal, and it says {}", animal.noise());
}