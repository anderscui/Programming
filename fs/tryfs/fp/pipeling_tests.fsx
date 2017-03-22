(+) 2 3 |> ignore

let fahrenheitToCelsius degreesF = (degreesF - 32.0) * 5.0 / 9.0

let marchHighTemps = [ 33.0; 30.0; 33.0; 38.0; 36.0; 31.0; 35.0;
                       42.0; 53.0; 65.0; 59.0; 42.0; 31.0; 41.0;
                       49.0; 45.0; 37.0; 42.0; 40.0; 32.0; 33.0;
                       42.0; 48.0; 36.0; 34.0; 38.0; 41.0; 46.0;
                       54.0; 57.0; 59.0 ]

// forward
marchHighTemps
|> List.average
|> fahrenheitToCelsius
|> printfn "March Average (C): %f"

// backward
printfn "March Average (C): %f" <| fahrenheitToCelsius (List.average(marchHighTemps))

// noncurried funcs
0.1 |> System.TimeSpan.FromSeconds |> System.Threading.Thread.Sleep

// composition
let averageInCelsius = List.average >> fahrenheitToCelsius
let delay = System.TimeSpan.FromSeconds >> System.Threading.Thread.Sleep
