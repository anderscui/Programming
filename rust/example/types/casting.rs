#![allow(overflowing_literals)]

fn main() {
    let decimal = 65.4321_f32;

    // no implicit conversion
    // let integer: u8 = decimal;

    let integer = decimal as u8;
    let ch = integer as char;

    println!("size of ch: {}", std::mem::size_of_val(&ch));

    // limitations in conversion
    // only `u8` can be cast as `char`, not `f32`
    // let ch2 = decimal as char;

    println!("Casting: {} -> {} -> {}", decimal, integer, ch);

    // value to unsigned type
    println!("1000 as a u16 is: {}", 1000 as u16);
    // 1000 - 256 - 256 - 256 = 232
    println!("1000 as a u8 is : {}", 1000 as u8);
    // -1 + 256 = 255
    println!("  -1 as a u8 is : {}", (-1i8) as u8);
}