#![allow(unused)]

extern crate aoc_rust;
use aoc_rust::aoc_utils::*;
use std::*;

const SAMPLE: &str = "190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20";

fn main() {
    let inp = &read_in();
    // both inp and sample are &str to avoid ownership issues; use String::from(_) or _.to_owned() or _.to_string() to get a non-sizable version

    let lines = lines(inp);
    let mut total = 0;
    let mut line_count = 0;
    for line in &lines {
        // println!("line {:<3}/{:<3}", line_count, lines.len());
        line_count += 1;
        let parts = line.split(":").collect::<Vec<_>>();
        let target = ints(parts[0])[0] as i64;
        let constituents = ints(parts[1]).iter().map(|x| *x as i64).collect::<Vec<_>>();
        for options in product_repeat((vec![0, 1]).iter(), constituents.len() - 1) {
            let mut value = constituents[0];
            for i in 0..constituents.len() - 1 {
                if options[i] == &0 {
                    value += constituents[i + 1];
                } else if options[i] == &1 {
                    value *= constituents[i + 1];
                }
            }
            if value == target {
                total += target;
                break;
            }
        }
    }
    println!("part 1: {:?}", total);
    let mut total = 0;
    let mut line_count = 0;
    for line in &lines {
        // println!("line {:<3}/{:<3}", line_count, lines.len());
        line_count += 1;
        let parts = line.split(":").collect::<Vec<_>>();
        let target = ints(parts[0])[0] as i64;
        let constituents = ints(parts[1]).iter().map(|x| *x as i64).collect::<Vec<_>>();
        for options in product_repeat((vec![0, 1, 2]).iter(), constituents.len() - 1) {
            let mut value = constituents[0];
            for i in 0..constituents.len() - 1 {
                let v = constituents[i + 1];
                if options[i] == &0 {
                    value += v;
                } else if options[i] == &1 {
                    value *= v;
                } else {
                    value = strtoint(&format!("{}{}", value, v));
                }
                if (value > target) {
                    break;
                }
            }
            if value == target {
                total += target;
                break;
            }
        }
    }
    println!("part 2: {:?}", total);
}
