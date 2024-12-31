#![allow(unused)]

extern crate aoc_rust;
use aoc_rust::aoc_utils::*;
use regex::Regex;
use std::*;

const SAMPLE: &str = "47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,97,47,61,53
61,13,29
97,13,75,29,47";

fn main() {
    let inp = &read_in();

    // both inp and sample are &str to avoid ownership issues; use String::from(_) or _.to_owned() or _.to_string() to get a non-sizable version
    let rules: Vec<_> = lines(inp.split("\n\n").collect::<Vec<_>>()[0])
        .into_iter()
        .map(|a| {
            let parts: Vec<_> = a.split("|").collect();
            (parts[0].to_string(), parts[1].to_string())
        })
        .collect();
    let seqs: Vec<i32> = lines(inp.split("\n\n").collect::<Vec<_>>()[1])
        .into_iter()
        .map(|a| a.split(",").map(|s| s.to_string()).collect::<Vec<_>>())
        .map(|seq| {
            if (0..seq.len()).all(|idx| {
                (idx + 1..seq.len()).all(|b| rules.contains(&&(seq[idx].clone(), seq[b].clone())))
            }) {
                return strtoint(&seq[(seq.len() / 2) as usize]);
            }
            return 0;
        })
        .collect();
    println!("part 1: {:?}", seqs.iter().sum::<i32>());

    let seqs: i32 = lines(inp.split("\n\n").collect::<Vec<_>>()[1])
        .into_iter()
        .map(|a| a.split(",").map(|s| s.to_string()).collect::<Vec<_>>())
        .filter(|seq| {
            !(0..seq.len()).all(|idx| {
                (idx + 1..seq.len()).all(|b| rules.contains(&&(seq[idx].clone(), seq[b].clone())))
            })
        })
        .map(|seq| {
            let amounts: Vec<_> = seq
                .iter()
                .map(|e| {
                    return rules
                        .iter()
                        .filter(|rule| rule.0 == *e && seq.contains(&rule.1))
                        .count();
                })
                .collect();
            let mid_idx = amounts
                .iter()
                .position(|&x| x == seq.len() / 2)
                .expect("should find middle element");
            strtoint(&seq[mid_idx])
        })
        .sum::<i32>();
    println!("part 2: {:?}", seqs);
}
