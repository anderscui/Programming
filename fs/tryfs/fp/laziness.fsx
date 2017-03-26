let lazy_op = lazy (printfn "evaluating lazy exp"
                    System.Threading.Thread.Sleep(1000)
                    42)

#time "on"

// Force() is same as Value prop.
lazy_op.Force() |> printfn "Result: %i"

lazy_op.Force() |> printfn "Result: %i"
lazy_op.Force() |> printfn "Result: %i"

#time "off"