#[cfg(target_os = "linux")]
fn are_you_on_linux() {
    println!("You are running linux.");
}

#[cfg(not(target_os = "linux"))]
fn are_you_on_linux() {
    println!("You are *not* running linux.");
}

fn main() {
    are_you_on_linux();

    println!("are you sure?");
    if cfg!(target_os = "linux") {
        println!("Yes, it's definitely linux.");
    } else {
        println!("Yes, it's definitely *not* linux.");
    }
}