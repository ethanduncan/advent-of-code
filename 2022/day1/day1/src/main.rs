use std::fs;

fn main() {

    let binding = fs::read_to_string("../input.txt")
        .expect("Should have been able to read the file");
    let contents: Vec<&str> = binding.split("\n")
        .collect();

    let mut current = 0;
    let mut large = 0;
    for thing in contents.iter() {
        if thing.is_empty(){
            if current > large {
                large = current;
            }
            println!("total is {}", current);
            current = 0;
            continue;
        }
        current += thing.parse::<i32>().unwrap();
    }

    println!("{}", large);

}
