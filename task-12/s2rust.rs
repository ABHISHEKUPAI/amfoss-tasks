use std::io;

fn main() {
    println!("Enter height:");
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();

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
