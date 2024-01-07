use std::fmt;

fn reverse(pair: (i32, bool)) -> (bool, i32) {
    let (first, second) = pair;
    (second, first)
}

fn transpose(matrix: Matrix) -> Matrix {
    Matrix(matrix.0, matrix.2, matrix.1, matrix.3)
}

#[derive(Debug)]
struct Matrix(f32, f32, f32, f32);

impl fmt::Display for Matrix {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "( {}, {} )\n", self.0, self.1)?;
        write!(f, "( {}, {} )", self.2, self.3)
    }
}

fn main() {
    // A tuple with a bunch of different types.
    let long_tuple = (1u8, 2u16, 3u32, 4u64,
        -1i8, -2i16, -3i32, -4i64,
        0.1f32, 0.2f64,
        'a', true);
    
    // tuple indexing
    println!("first: {}, second: {}", long_tuple.0, long_tuple.1);

    let pair = (1, true);
    println!("pair: {:?}, reversed: {:?}", pair, reverse(pair));

    let matrix = Matrix(1.1, 1.2, 2.1, 2.2);
    println!("{:?}", matrix);
    println!("{}", matrix);
    println!("transposed:");
    println!("{}", transpose(matrix));
}