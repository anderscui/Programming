use clap::{App, Arg};

fn main() {
    // run: cargo run -- -n hello world
    // separate cargo and args

    // format the output in a debugging context.
    // println!("{:?}", std::env::args());

    // _ means: do not use it right now
    let _matches = App::new("echor")
                    .version("0.1.0")
                    .author("Echo <echo@gmail.com>")
                    .about("Rust echo.")  // a short desc for app
                    .arg(Arg::with_name("text")
                              .value_name("TEXT")
                              .help("Input text")
                              .required(true)
                              .min_values(1),
                    )
                    .arg(Arg::with_name("omit_newline")
                              .short("n")
                              .help("Do not print newline")
                              .takes_value(false),
                    )
                    .get_matches();
    
    // pretty print the args
    // println!("{:#?}", _matches);

    let text = _matches.values_of_lossy("text").unwrap();
    let omit_newline = _matches.is_present("omit_newline");
    
    // let mut ending = "\n";
    // if omit_newline {
    //     ending = "";
    // }
    let ending = if omit_newline { "" } else { "\n" };
    print!("{}{}", text.join(" "), ending);
}
