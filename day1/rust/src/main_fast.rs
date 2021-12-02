use std::fs::File;
use std::io::prelude::*;
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
    let mut answer1 = 0;
    let mut answer2 = 0;
    for i in 0..ns.len(){
        if i + 3 < ns.len(){
            if ns[i] < ns[i + 3]{
                answer2 += 1;
            }
            if ns[i] < ns[i + 1]{
                answer1 += 1;
            }
        }
    }

    println!("Answer(1): {}", answer1);
    println!("Answer(2): {}", answer2);
}