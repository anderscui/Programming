type Color = 
  | Red 
  | Green 
  | Blue

let c1 = Color.Green

let likes = function
  | Green | Blue -> true
  | _ -> false
  
open System

[<Flags>]
type DayOfWeek =
  | None = 0
  | Sunday = 1
  | Monday = 2
  | Tuesday = 4
  | Wednesday = 8
  | Thursday = 16
  | Friday = 32
  | Saturday = 64
  | Weekdays = 62
  | WeekendDays = 65

let today = DayOfWeek.Sunday
let ans1 = DayOfWeek.Monday.HasFlag DayOfWeek.WeekendDays
let ans2 = DayOfWeek.Weekdays.HasFlag DayOfWeek.Wednesday
let ans3 = enum<DayOfWeek> 32