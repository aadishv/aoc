#![allow(unused)]

extern crate aoc_rust;
use aoc_rust::aoc_utils::*;
use std::*;

const SAMPLE: &str = "3   4
4   3
2   5
1   3
3   9
3   3
";
fn main() {
    let sample = String::from(SAMPLE);
    let lines = lines(read_in())
        .iter()
        .map(|x| ints(x.clone()))
        .collect::<Vec<_>>();
    let mut x = Vec::<i32>::new();
    let mut y = Vec::<i32>::new();
    for l in lines {
        x.push(l[0]);
        y.push(l[1]);
    }

    let mut a = x.clone();
    let mut b = y.clone();
    a.sort();
    b.sort();
    let mut total: i32 = iter::zip(a, b)
        .map(|o| -> i32 {
            return (o.0 - o.1).abs();
        })
        .sum();
    println!("part 1: {:?}", total);
    //

    let total: i32 = x
        .iter()
        .map(|x| x * (y.iter().filter(|&p| p == x).count() as i32))
        .sum();
    println!("part 2: {}", total);
}
