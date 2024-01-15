use std::collections::HashMap;

struct Counter {
    count: u32,
}

impl Counter {
    fn new() -> Counter {
        Counter { count: 0 }
    }
}

impl Iterator for Counter {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        if self.count < 5 {
            self.count += 1;
            Some(self.count)
        } else {
            None
        }
    }
}

fn main() {
    let arr = [1, 2, 3];
    let mut arr_iter = arr.into_iter();

    // next change internal state of iterator, so `mut` is required.
    assert_eq!(arr_iter.next(), Some(1));
    assert_eq!(arr_iter.next(), Some(2));
    assert_eq!(arr_iter.next(), Some(3));
    assert_eq!(arr_iter.next(), None);

    // simulate `for`
    let arr = [1, 2, 3];
    {
        let _result = match IntoIterator::into_iter(arr) {
            mut iter => loop {
                match iter.next() {
                    Some(x) => { println!("{}", x); }
                    None => break,
                }
            },
        };
    }

    // mut iter
    let mut values = vec![1, 2, 3];
    let mut values_iter_mut = values.iter_mut();
    if let Some(v) = values_iter_mut.next() {
        *v = 0;
    }
    println!("{:?}", values);

    // collect
    let v1 = vec![1, 2, 3];
    let v2: Vec<_> = v1.iter().map(|x| x + 1).collect();
    println!("{:?}", v2);

    let names = ["anders", "bill"];
    let ages = [20, 30];
    let folks: HashMap<_, _> = names.into_iter().zip(ages.into_iter()).collect();
    println!("{:?}", folks);

    // Counter
    let mut counter = Counter::new();
    assert_eq!(counter.next(), Some(1));
    assert_eq!(counter.next(), Some(2));
    assert_eq!(counter.next(), Some(3));
    assert_eq!(counter.next(), Some(4));
    assert_eq!(counter.next(), Some(5));
    assert_eq!(counter.next(), None);

    // beyond next
    let sum: u32 = Counter::new()
        .zip(Counter::new().skip(1))
        .map(|(a, b)| a * b)
        .filter(|x| x % 3 == 0)
        .sum();
    assert_eq!(18, sum);

    // enumerate
    let v = vec![1u64, 2, 3, 4, 5, 6];
    let val = v.iter()
        .enumerate()
        .filter(|(i, _)| i % 2 == 0)
        .map(|(_, val)| val)
        .fold(0u64, |sum, acm| sum + acm);
    println!("{}", val);
}