use std::convert::identity;
use std::thread;
use std::time::Duration;

fn workout(intensity: u32, random_number: u32) {
    let action = || {
        println!("muuu...");
        thread::sleep(Duration::from_secs(1));
        intensity
    };

    if intensity < 25 {
        println!("今天做 {} 个俯卧撑！", action());
    } else if random_number == 3 {
        println!("今天休息下吧。。。");
    } else {
        println!("今天有氧跑步 {} 分钟：）", action());
    }
}

fn main() {
    let intensity = 60;
    let random_num = 3;
    workout(intensity, random_num);

    // let sum = |x, y| x + y;
    // let v = sum(1, 2);
}