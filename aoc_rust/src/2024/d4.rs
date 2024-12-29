#![allow(unused)]

extern crate aoc_rust;
use aoc_rust::aoc_utils::*;
use regex::Regex;
use std::*;

const SAMPLE: &str = "MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX";

fn main() {
    let inp = &read_in();
    let grid = Grid::fromstr(inp, '+');
    println!("{} {}", grid.width, grid.height);

    // Pre-calculate valid coordinates as a HashSet for O(1) lookup
    let valid_coords = grid.valid_coords();

    let queue = grid
        .all_coords()
        .into_iter()
        .filter(|&coord| grid[coord] == 'X')
        .map(|coord| {
            coord
                .neighbors()
                .into_iter()
                .filter(|&n| valid_coords.contains(&n) && grid[n] == 'M')
                .filter(|&n| {
                    let diff = (n as i32) - (coord as i32);
                    if let (Some(ac), Some(sc)) = (coord.addi32(diff * 2), coord.addi32(diff * 3)) {
                        valid_coords.contains(&ac)
                            && valid_coords.contains(&sc)
                            && grid[ac] == 'A'
                            && grid[sc] == 'S'
                    } else {
                        false
                    }
                })
                .count()
        })
        .sum::<usize>();

    println!("part 1: {:?}", queue);
    println!("part 2: {:?}", 0);
}
