open OUnit2
open Tdd

let make_weekday_test name expected_output input =
  name >:: (fun _ -> assert_equal expected_output (next_weekday input))


let tests = "test suite for sum" >::: [
  make_weekday_test "tue_after_mon" Tuesday Monday;
  make_weekday_test "wed_after_tue" Wednesday Tuesday;
  make_weekday_test "thu_after_wed" Thursday Wednesday;
  make_weekday_test "fri_after_thu" Friday Thursday;
  make_weekday_test "mon_after_fri" Monday Friday;
  make_weekday_test "mon_after_sat" Monday Saturday;
  make_weekday_test "mon_after_sun" Monday Sunday;
]

let _ = run_test_tt_main tests
