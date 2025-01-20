#![allow(unused)]

extern crate aoc_rust;
use aoc_rust::aoc_utils::*;
use std::collections::*;
use std::*;

const SAMPLE: &str = "..........
..........
..........
....a.....
........a.
.....a....
..........
..........
..........
..........
";

fn main() {
    let inp = &read_in();
    // both inp and sample are &str to avoid ownership issues; use String::from(_) or _.to_owned() or _.to_string() to get a non-sizable version
    let mut grid = Grid::fromstr(SAMPLE, '.');
    let mut antennas: HashMap<char, Vec<u16>> = HashMap::new();
    for c in grid
        .valid_coords()
        .iter()
        .map(|&c| grid[c])
        .collect::<HashSet<char>>()
    {
        if c == '.' {
            continue;
        }
        antennas.insert(
            c,
            grid.valid_coords()
                .iter()
                .filter(|&a| grid[*a] == c)
                .map(|&a| a as u16)
                .collect(),
        );
    }
    let mut antinodes: HashSet<u16> = HashSet::new();
    for c in antennas.keys() {
        for ai in 0..antennas[c].len() {
            for bi in ai + 1..antennas[c].len() {
                let a = antennas[c][ai];
                let b = antennas[c][bi];
                if a != b {
                    let diff = (a as i16 - b as i16);
                    let antinode1 = (b as i16) + 2 * diff;
                    let antinode2 = (b as i16) - 1 * diff;
                    println!("{:?} {:?}", antinode1, antinode2);
                    if grid
                        .valid_coords()
                        .iter()
                        .map(|&c| c as i16)
                        .any(|c| c == antinode2)
                    {
                        antinodes.insert(antinode1 as u16);
                    }
                    if grid
                        .valid_coords()
                        .iter()
                        .map(|&c| c as i16)
                        .any(|c| c == antinode2)
                    {
                        antinodes.insert(antinode2 as u16);
                    }
                }
            }
        }
    }
    for &a in &antinodes {
        grid[a] = '#';
    }
    println!("part 1: {}", grid);
    println!("part 2: {:?}", 0);
}
