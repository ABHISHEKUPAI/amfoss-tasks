use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Unable to read file");
    let n: usize = contents.trim().parse().expect("Not a number");

    for i in 1..=n {
        let spaces = " ".repeat(n - i);

        if i == 1 {
            println!("{}*", spaces);
        } else if i == n {
            println!("{}", "*".repeat(2 * n - 1));
        } else {
            let inner_spaces = " ".repeat(2 * i - 3);
            println!("{}*{}*", spaces, inner_spaces);
        }
    }
}
