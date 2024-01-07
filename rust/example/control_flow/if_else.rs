fn main() {
    let x = 2;
    let y = 
        if x % 2 == 0 {
            1
        } else {
            0
        };
    println!("x = {}, y = {}", x, y);
}