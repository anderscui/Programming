let regs = Map.ofList [("a1", ("cheese", 25));
                       ("a2", ("herring", 4));
                       ("a3", ("soft drink", 5))]

let regs2 = Map.add "a4" ("bread", 6) regs

let has_expensive = Map.exists (fun _ (_, price) -> price > 20) regs

