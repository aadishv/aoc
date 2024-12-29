#![allow(unused)]

extern crate aoc_rust;
use aoc_rust::aoc_utils::*;
use std::*;

fn main() {
    let lines: Vec<Vec<i32>> = lines(read_in())
        .iter()
        .map(|x| ints(x.clone()))
        .collect::<_>();
    let diffs = lines
        .iter()
        .map(|x| list_diff(x.clone()))
        .collect::<Vec<Vec<i32>>>();
    let mut total = 0;
    println!("running");
    fn check_good(line: Vec<i32>) -> bool {
        let diff = list_diff(line);
        let all_iord = diff.iter().all(|&x| (x > 0)) || diff.iter().all(|&x| x < 0);
        let diff_inb = diff.iter().all(|x| (1..=3).contains(&x.abs()));
        all_iord && diff_inb
    }
    for (line, diff) in std::iter::zip(lines.clone(), diffs) {
        total += (check_good(line) as i32);
    }
    println!("part 1: {}", total);
    let mut total = 0;

    for line in lines {
        for changed in 0..line.len() {
            let mut found = false;
            let mut newl = line.clone();
            newl.remove(changed);
            if check_good(newl) {
                total += 1;
                found = true;
                break;
            }
            if found {
                break;
            }
        }
    }
    println!("part 2: {}", total)
}
