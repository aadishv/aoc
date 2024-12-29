#![allow(unused)]

extern crate aoc_rust;
use aoc_rust::aoc_utils::*;
use regex::Regex;
use std::*;

const SAMPLE: &str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))";

fn main() {
    let inp = &read_in();
    let lines = lines(inp.to_string());
    let regex = Regex::new(r"(mul\(\d+,\d+\))").unwrap();
    let sample = String::from(SAMPLE);
    println!(
        "part 1: {:?}",
        matches(regex, inp.to_string())
            .into_iter()
            .map(|x| ints(x.clone())[0] * ints(x.clone())[1])
            .sum::<i32>()
    );

    let re = Regex::new(r"(mul\(\d+,\d+\))|(do\(\))|(don\'t\(\))").unwrap();
    let mut flag = true;
    let mut total = 0;
    for m in matches(re, inp.to_string()) {
        if m.contains("'") {
            flag = false;
        } else if m == "do()" {
            flag = true;
        } else {
            if flag {
                total += ints(m.clone())[0] * ints(m.clone())[1];
            }
        }
    }
    println!("part 2: {}", total);
}
