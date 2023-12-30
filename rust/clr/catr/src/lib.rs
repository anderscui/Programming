use std::any::type_name;
use std::error::Error;
use std::fs::{File, read_to_string};
use std::io::{self, BufRead, BufReader};

use clap::{App, Arg};

// derive: add a trait

#[derive(Debug)]
pub struct Config {
    files: Vec<String>,
    number_lines: bool,
    number_nonblank_lines: bool,
}

type MyResult<T> = Result<T, Box<dyn Error>>;

fn type_of<T>(_: T) -> &'static str {
    type_name::<T>()
}

pub fn get_args() -> MyResult<Config> {
    // use `-` for STDIN.
    let matches = App::new("catr")
                    .version("0.1.0")
                    .author("Anders <anders@gmail.com>")
                    .about("Rust cat.")  // a short desc for app
                    .arg(Arg::with_name("files")
                              .value_name("FILE")
                              .help("Input file(s)")
                              .multiple(true)
                              .default_value("-"),
                    )
                    .arg(Arg::with_name("number_lines")
                              .short("n")
                              .long("number")
                              .help("Number the output lines, starting at 1.")
                              .takes_value(false)
                              .conflicts_with("number_nonblank_lines"),
                    )
                    .arg(Arg::with_name("number_nonblank_lines")
                              .short("b")
                              .long("number-nonblank")
                              .help("Number the non-blank lines, starting at 1.")
                              .takes_value(false),
                    )
                    .get_matches();

    let files = matches.values_of_lossy("files").unwrap();
    let number_lines = matches.is_present("number_lines");
    let number_nonblank_lines = matches.is_present("number_nonblank_lines");
    
    Ok(Config {
        files: files,
        number_lines: number_lines,
        number_nonblank_lines: number_nonblank_lines,
    })
}

fn open(filename: &str) -> MyResult<Box<dyn BufRead>> {
    match filename {
        "-" => Ok(Box::new(BufReader::new(io::stdin()))),
        _ => Ok(Box::new(BufReader::new(File::open(filename)?))),
    }
}

pub fn run(config: Config) -> MyResult<()> {
    // print the config.
    // dbg!(config);
    for filename in config.files {
        match open(&filename) {
            Err(err) => eprintln!("Failed to open {}: {}", filename, err),
            Ok(file) => { 
                let mut last_nonblank_index = 0;
                for (line_index, line_result) in file.lines().enumerate() {
                    let line = line_result?;
                    
                    if config.number_lines {
                        // right-justified field.
                        println!("{:>6}\t{}", line_index+1, line);
                    } else if config.number_nonblank_lines {
                        if !line.is_empty() {
                            last_nonblank_index += 1;
                            println!("{:>6}\t{}", last_nonblank_index, line);
                        } else {
                            println!("{}", line);
                        }
                    } else {
                        println!("{}", line);
                    }
                }
            },
        }
    }
    Ok(())
}