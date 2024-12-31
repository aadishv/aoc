#![allow(unused)]

extern crate aoc_rust;
use aoc_rust::aoc_utils::*;
use std::*;

const sample: &str = "";

fn main() {
    let inp = &read_in();
    // both inp and sample are &str to avoid ownership issues; use String::from(_) or _.to_owned() or _.to_string() to get a non-sizable version
    let lines = lines(sample.to_string());

    println!("part 1: {:?}", 0);
    println!("part 2: {:?}", 0);
}
