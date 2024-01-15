use std::collections::HashMap;

fn main() {
    let teams = vec![
        ("中国队".to_string(), 100),
        ("美国队".to_string(), 10),
        ("日本队".to_string(), 50),
    ];

    let team_scores: HashMap<_, _> = teams.into_iter().collect();
    println!("{:?}", team_scores);

    let team_name = String::from("中国队");
    let score = team_scores.get(&team_name);
    match score {
        Some(s) => println!("score of {team_name}: {s}"),
        None => println!("no score for {team_name}"),
    }

    // iterate
    for (k, v) in &team_scores {
        println!("{k}: {v}");
    }
}