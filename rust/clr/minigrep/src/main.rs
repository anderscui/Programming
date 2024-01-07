use std::{env, process};

use minigrep::Config;

fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("problem parsing args: {err}");
        process::exit(1);
    });

    println!("searching for {}", config.query);
    println!("... in file {}", config.file_path);

    if let Err(e) = minigrep::run(config) {
        eprintln!("app error: {e}");
        process::exit(1);
    }
}