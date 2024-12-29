#![allow(unused)]

use regex::Regex;
use std::collections::HashMap;
use std::fmt;
use std::io::{self, Read};
use std::ops::{Index, IndexMut};

#[derive(fmt::Debug)]
pub struct Grid<T: Copy + fmt::Display> {
    pub grid: HashMap<u16, T>,
    pub width: u8,
    pub height: u8,
    pub default: T,
}

impl<T: fmt::Display + Copy> fmt::Display for Grid<T> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let mut size: usize = 0;
        for y in 0..self.height {
            for x in 0..self.width {
                let i = (x as u16) * 256 + (y as u16);
                let v: T = self.grid.get(&i).copied().unwrap_or(self.default);
                let value = format!("{}", v);
                if value.len() > size {
                    size = value.len().into();
                }
            }
        }
        size += 1;

        let padding: usize = ((self.width as usize) * size - size + 1).into();
        write!(
            f,
            "\n{0:-<1$}",
            format!("{0}x{1}", self.width, self.height),
            padding
        )?;
        for y in 0..self.height {
            write!(f, "\n")?;
            for x in 0..self.width {
                let i = (x as u16) * 256 + (y as u16);
                let value: T = self.grid.get(&i).copied().unwrap_or(self.default);
                write!(f, "{0:<1$}", value, size)?;
            }
        }
        Ok(())
    }
}
impl<T: fmt::Display + Copy> Index<(u8, u8)> for Grid<T> {
    type Output = T;

    fn index(&self, (x, y): (u8, u8)) -> &Self::Output {
        let idx = (x as u16) * 256 + (y as u16);
        self.grid.get(&idx).unwrap_or(&self.default)
    }
}
impl<T: fmt::Display + Copy> IndexMut<(u8, u8)> for Grid<T> {
    fn index_mut(&mut self, (x, y): (u8, u8)) -> &mut Self::Output {
        let idx = (x as u16) * 256 + (y as u16);
        self.grid.entry(idx).or_insert(self.default)
    }
}
impl<T: fmt::Display + Copy> Index<u16> for Grid<T> {
    type Output = T;
    fn index(&self, idx: u16) -> &Self::Output {
        self.grid.get(&idx).unwrap_or(&self.default)
    }
}
impl<T: fmt::Display + Copy> IndexMut<u16> for Grid<T> {
    fn index_mut(&mut self, idx: u16) -> &mut Self::Output {
        self.grid.entry(idx).or_insert(self.default)
    }
}
impl<T: fmt::Display + Copy> Grid<T> {
    pub fn idx(&self, x: u8, y: u8) -> u16 {
        (x as u16) * 256 + (y as u16)
    }
}
pub trait PointRepr<PointMod>
where
    Self: Sized,
{
    const SDIRS: [PointMod; 4];
    const DDIRS: [PointMod; 4];
    const DIRS: [PointMod; 8];
    fn diag_nbors(&self) -> [Self; 4];
    fn straight_nbors(&self) -> [Self; 4];
    fn neighbors(&self) -> [Self; 8];
    fn idx(x: u8, y: u8) -> Self;
}
impl PointRepr<i16> for u16 {
    const SDIRS: [i16; 4] = [256, -256, 1, -1];
    const DDIRS: [i16; 4] = [257, 255, -255, -257];
    const DIRS: [i16; 8] = [256, -256, 1, -1, 257, 255, -255, -257];
    fn straight_nbors(&self) -> [u16; 4] {
        return u16::DDIRS.map(|x| (x + (*self as i16)) as u16);
    }
    fn diag_nbors(&self) -> [u16; 4] {
        return u16::SDIRS.map(|x| (x + (*self as i16)) as u16);
    }
    fn neighbors(&self) -> [u16; 8] {
        return u16::DIRS.map(|x| (x + (*self as i16)) as u16);
    }
    fn idx(x: u8, y: u8) -> u16 {
        (x as u16) * 256 + (y as u16)
    }
}
impl<T: fmt::Display + Copy> Grid<T> {
    pub fn create_grid(width: u8, height: u8, default: T) -> Self {
        let mut grid = HashMap::new();
        for x in 0..width {
            for y in 0..height {
                let i: u16 = (x as u16) * 256 + (y as u16);
                grid.insert(i, default);
            }
        }
        return Grid {
            grid: grid,
            width: width,
            height: height,
            default: default,
        };
    }
}

pub fn read_in() -> String {
    let mut buffer = String::new();
    match io::stdin().read_to_string(&mut buffer) {
        Ok(_) => return buffer,
        Err(error) => panic!("couldn't read input"),
    };
}
pub fn lines(string: String) -> Vec<String> {
    string
        .split('\n')
        .map(|x| String::from(x))
        .filter(|x| *x != String::from(""))
        .collect::<Vec<_>>()
}
pub fn strtoint(string: String) -> i32 {
    match string.parse::<i32>() {
        Ok(n) => return n,
        Err(e) => panic!("Failed to convert '{}' to a number", string),
    }
}
pub fn ints(string: String) -> Vec<i32> {
    let re = Regex::new(r"-?\d+").unwrap();
    return re
        .find_iter(&string)
        .map(|x| string[x.start()..x.end()].to_string())
        .map(|x| strtoint(x))
        .collect::<Vec<_>>();
}

pub fn list_diff<T: std::ops::Sub<Output = T> + Copy>(list: Vec<T>) -> Vec<T> {
    (1..list.len())
        .map(|x| list[x] - list[x - 1])
        .collect::<Vec<T>>()
}
