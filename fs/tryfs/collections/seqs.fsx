// use yield and yield!
let seq1 = seq { yield "a"; yield "b" }
let strange = seq {
  yield 1;
  yield 2;

  yield! [5..10]

  yield! seq {
    for i in 1..10 do
      if i % 2 = 0 then yield i }
}

strange |> Seq.toList

