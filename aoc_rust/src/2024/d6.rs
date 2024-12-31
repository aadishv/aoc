#![allow(unused)]

extern crate aoc_rust;
use aoc_rust::aoc_utils::*;
use std::collections::*;
use std::*;

const SAMPLE: &str = "....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...";

fn main() {
    let inp = &read_in();
    // both inp and sample are &str to avoid ownership issues; use String::from(_) or _.to_owned() or _.to_string() to get a non-sizable version
    let grid = Grid::fromstr(inp, ' ');
    let valid = grid.valid_coords();
    let mut guard: u16 = *valid
        .iter()
        .find(|&x| grid[*x] == '^')
        .expect("guard pos slay");
    let mut guard_dir: i32 = -1; // up
    let mut sdirs = [-1, 256, 1, -256].iter();
    let mut set = collections::HashSet::new();
    while valid.contains(&guard) {
        set.insert(guard);
        let next_pos = guard.addi32(guard_dir);
        if next_pos == None {
            break;
        }
        let next_pos = next_pos.expect("just checked...");
        if grid[next_pos] == '#' {
            let pos = sdirs.clone().position(|x| *x == guard_dir).expect("fdghsd");
            // println!("{} {} p", pos, sdirs.clone().collect::<Vec<_>>()[pos]);
            guard_dir = *sdirs.clone().collect::<Vec<_>>()[((pos + 1) % 4)];
        }
        let next_pos = guard.addi32(guard_dir);
        if next_pos == None {
            break;
        }
        guard = next_pos.expect("just checked...?");
    }
    let guard = *valid
        .iter()
        .find(|&x| grid[*x] == '^')
        .expect("guard pos slay");
    println!("part 1: {:?}", set.len());
    let mut mysdirs = collections::HashMap::<i32, i32>::new();
    mysdirs.insert(-1, 256);
    mysdirs.insert(256, 1);
    mysdirs.insert(1, -256);
    mysdirs.insert(-256, -1);
    fn update_g_w_p(g: Grid<char>, p: Vec<u16>) -> Grid<char> {
        let mut mygg = g.clone();
        for pp in p {
            mygg[pp] = 'X';
        }
        return mygg;
    }
    let valid: collections::HashSet<i32> = valid.iter().map(|&p| p as i32).collect();

    let max_iterations = (grid.width as usize) * (grid.height as usize) * 4;

    let mut check_for_loop = |ppp: i32| -> bool {
        let mut myg = guard as i32;
        let mut guard_dir: i32 = -1; // up
        let mut visited = HashSet::<(i32, i32)>::new();

        for _ in 0..max_iterations {
            if visited.contains(&(myg, guard_dir)) {
                return true;
            }
            visited.insert((myg, guard_dir));

            let next_pos = myg + guard_dir;
            if grid[next_pos as u16] == '#' || next_pos == ppp {
                guard_dir = mysdirs[&guard_dir];
            } else {
                if !valid.contains(&next_pos) {
                    return false;
                }
                myg += guard_dir;
            }
        }
        false
    };
    let mut i = 0;

    let potential_positions: Vec<i32> = set
        .iter()
        .filter(|&pos| grid[*pos] == '.' && *pos != guard)
        .map(|&pos| pos as i32)
        .collect();
    let t = potential_positions.len();
    let total = potential_positions
        .into_iter() // parallel processing
        .filter(|&pos| {
            println!("{} {}", i, t);
            i += 1;
            check_for_loop(pos)
        })
        .count();
    println!("part 2: {:?}", total);
    // i thought using a compiled language would make brute force viable...
    // haha nope sucker
}
