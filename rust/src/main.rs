use std::fs::File;
use std::io::prelude::*;
use std::time::Instant;
fn main() {
    let mut ns = String::new();
    File::open("x")
        .unwrap()
        .read_to_string(&mut ns)
        .expect("cannot read file");

    let ns = ns
        .split("\n")
        .into_iter()
        .map(|x| x.parse::<i32>().unwrap())
        .collect::<Vec<_>>();
    fn p(x: usize, ns: Vec<i32>) -> i32 {
        let mut count = 0;
        let mut last: i32 = 0;
        let w = ns.windows(x);
        let mut index: u32 = 0;
        for i in w {
            let sum: i32 = i.into_iter().sum();
            if index > 0 {
                if &last < &sum {
                    count += 1;
                }
            }
            last = sum;
            index = index + 1;
        }
        count
    }
    let start = Instant::now();
    let x = p(1, ns.clone());
    let y = p(3, ns.clone());
    let end = Instant::now();
    println!("Total time: {:?}", end - start);
    println!("x (1): {}", x);
    println!("x (2): {}", y);
}