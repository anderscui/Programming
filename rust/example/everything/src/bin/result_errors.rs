use std::fs::File;
use std::{fs, io};
use std::io::Read;

fn read_file() -> Result<String, io::Error> {
    let mut f = File::open("hello.txt")?;
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    Ok(s)
}

fn read_file2() -> Result<String, io::Error> {
    let mut s = String::new();
    let mut f = File::open("hello.txt")?.read_to_string(&mut s)?;
    Ok(s)
}

fn read_file3() -> Result<String, io::Error> {
    fs::read_to_string("hello.txt")
}

fn main() {
    let contents = read_file3();
    match contents {
        Ok(s) => println!("contents: {s}"),
        Err(e) => println!("error: {e}"),
    };
}