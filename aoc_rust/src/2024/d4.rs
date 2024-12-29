#![allow(unused)]

extern crate aoc_rust;
use aoc_rust::aoc_utils::*;
use regex::Regex;
use std::*;

const SAMPLE: &str = ".M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........";

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
    // println!("{}", grid);
    let q = grid
        .all_coords()
        .into_iter()
        .filter(|coord| grid[*coord] == 'A')
        .filter(|coord| {
            let inw = (1..(grid.width - 1)).contains(&coord.to_coord().0);
            let inh = (1..(grid.height - 1)).contains(&coord.to_coord().1);
            if !(inw && inh) {
                return false;
            }
            let diag1 = [coord + 257, coord - 257].map(|x| grid[x]);
            let diag2 = [coord + 255, coord - 255].map(|x| grid[x]);

            // println!(
            //     "{:?} {:?} {:?} {:?} {:?}",
            //     coord.to_coord(),
            //     (coord + 257).to_coord(),
            //     (coord - 257).to_coord(),
            //     (coord + 254).to_coord(),
            //     (coord - 254).to_coord()
            // );
            return diag1.contains(&'M')
                && diag1.contains(&'S')
                && diag2.contains(&'M')
                && diag2.contains(&'S');
        })
        .count();

    println!("part 2: {:?}", q);
}
