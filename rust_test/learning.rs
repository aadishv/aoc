use std::fmt;
/*
Random notes:
* '' is used for characters (single letter), "" for one-line strings
* using {n} in a string, where n is an integer allows you to access the nth provided interpolator

*/

fn hello_world() {
    println!("Hello World!");
}

fn formatted_print() {
    // standard interpolation
    println!("My name is {} {}", "Aadish", 'V');
    println!(
        "My name is {my_first} {my_last}, and I know someone named {his_first} {his_last}.",
        his_last = "Sitaram",
        his_first = "Shiv",
        my_last = "Verma",
        my_first = "Aadish"
    );

    // printing numbers fancy
    println!("Base 10:               {:=>10}", 69420); // 69420
    println!("Base 2 (binary):       {:b}", 69420); // 10000111100101100
    println!("Base 8 (octal):        {:o}", 69420); // 207454
    println!("Base 16 (hexadecimal): {:x}", 69420); // 10f2c
    println!("Test: {number:$>width$}", number = 69420, width = 10);
    println!("My name is {0}, {1} {0}", "Bond", "James");

    let pi = 3.1415926535;
    println!("Pi is approx.         {pi:.4}"); // it rounds, not shaves!
}

#[derive(Debug)]
#[allow(dead_code)]
struct DebugPrintable(i32);

impl fmt::Display for DebugPrintable {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.0)
    }
}

#[derive(Debug)]
struct Complex {
    real: f64,
    imag: f64,
}

impl fmt::Display for Complex {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{0} + {1}i", self.real, self.imag)
    }
}

fn debug_print() {
    let my_debug_printable: DebugPrintable = DebugPrintable(64);
    println!("debug:     {my_debug_printable:?}",);
    println!("display:   {my_debug_printable:}",);
    // activity
    let my_compl_n: Complex = Complex {
        real: 3.3,
        imag: 7.2,
    };
    println!("debug:     {my_compl_n:?}");
    println!("display:   {my_compl_n:}");
    // fails without the above impl because std::fmt::Display isn't implemented for `DebugPrintable`
    /* 1.2.3 activity
    ```rust
    impl fmt::Display for Color {
        fn fmt(&self, f: &mut Formatter) -> fmt::Result {
            write!(
                f,
                "RGB ({0}, {1}, {2}) 0x{3:0>6x}",
                self.red,
                self.green,
                self.blue,
                self.red as u32 * 65536 + self.green as u32 * 256 + self.blue as u32
            )
        }
    }
    ```
    */
}

fn main() {
    println!("\nSECTION: hello_world -----\n");
    hello_world();
    println!("\nSECTION: formatted_print -----\n");
    formatted_print();
    println!("\nSECTION: debug_print -----\n");
    debug_print();
    let mystr = "Hello world!";
    println!("{:?}", mystr.get([0..5]));
}
