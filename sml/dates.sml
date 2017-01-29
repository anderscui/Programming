(*
fun date (year: int, month: int, day: int) =
	(year, month, day)

fun sum (nums: int list) =
	if null nums
	then 0
	else (hd nums) + sum(tl nums)

	*)

val month_names = ["January", "February", "March", "April",
				   "May", "June", "July", "August", "September", "October", "November", "December"]

val month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

fun is_older (date1: int * int * int, date2: int * int * int) =
	#1 date1 < #1 date2
	orelse (#1 date1 = #1 date2 andalso #2 date1 < #2 date2)
	orelse (#1 date1 = #1 date2 andalso #2 date1 = #2 date2 andalso #3 date1 < #3 date2)

fun number_in_month (dates: (int * int * int) list, month: int) =
	if null dates
	then 0
	else (if #2 (hd dates) = month then 1 else 0) + number_in_month (tl dates, month)

fun number_in_months (dates: (int * int * int) list, months: int list) =
	if null months
	then 0
	else number_in_month(dates, hd months) + number_in_months(dates, tl months)

fun dates_in_month (dates: (int * int * int) list, month: int) =
	if null dates
	then []
	else (if #2 (hd dates) = month 
		  then (hd dates) :: dates_in_month (tl dates, month) 
		  else dates_in_month (tl dates, month))

fun dates_in_months (dates: (int * int * int) list, months: int list) =
	if null months
	then []
	else dates_in_month(dates, hd months) @ dates_in_months(dates, tl months)

fun get_nth (strs: string list, n: int) =
	if n = 1
	then hd strs 
	else get_nth(tl strs, n-1)

fun date_to_string (date: int * int * int) =
	get_nth(month_names, #2 date) ^ " " ^ Int.toString(#3 date) ^ ", " ^ Int.toString(#1 date)

fun number_before_reaching_sum (sum: int, nums: int list) =
	let fun acc (cur_pos: int, cur_val: int, nums: int list) =
			if null nums
			then cur_pos
			else if cur_val + (hd nums) < sum
				 then acc (cur_pos + 1, cur_val + (hd nums), tl nums)
				 else cur_pos
	in
		acc(0, 0, nums)
	end

fun what_month (day: int) =
	number_before_reaching_sum(day, month_days) + 1

fun month_range (day1: int, day2: int) =
	if day1 > day2
	then []
	else what_month(day1) :: month_range(day1+1, day2)

fun oldest (dates: (int * int * int) list) =
	if null dates
	then NONE
	else
		let val tl_oldest = oldest(tl dates)
		in if isSome tl_oldest andalso is_older((valOf tl_oldest), (hd dates))
		   then tl_oldest
		   else SOME (hd dates)
		end

val ans1 = is_older((1900, 10, 10), (1901, 1, 10)) 
		   andalso is_older((1900, 1, 10), (1900, 2, 10))
		   andalso is_older((1900, 1, 10), (1900, 1, 11))
		   andalso (not(is_older((1900, 1, 10), (1900, 1, 10))))

val ans2 = number_in_month([(2011, 1, 10), (2012, 2, 15), (2012, 1, 15)], 1) = 2
		   andalso number_in_month([(2011, 1, 10), (2012, 2, 15), (2012, 1, 15)], 3) = 0

val ans3 = number_in_months([(2011, 1, 10), (2012, 2, 15), (2012, 1, 15)], [1]) = 2
		   andalso number_in_months([(2011, 1, 10), (2012, 2, 15), (2012, 1, 15)], [1, 2, 3]) = 3
		   andalso number_in_months([(2011, 1, 10), (2012, 2, 15), (2012, 1, 15)], [3]) = 0

val ans4 = dates_in_month([(2011, 1, 10), (2012, 2, 15), (2012, 1, 15)], 1) = [(2011, 1, 10), (2012, 1, 15)]
		   andalso dates_in_month([(2011, 1, 10), (2012, 2, 15), (2012, 1, 15)], 3) = []

val ans5 = dates_in_months([(2011, 1, 10), (2012, 2, 15), (2012, 1, 15)], [1]) = [(2011, 1, 10), (2012, 1, 15)]
		   andalso dates_in_months([(2011, 1, 10), (2012, 2, 15), (2012, 1, 15)], [1, 2, 3]) = 
		   		[(2011, 1, 10), (2012, 1, 15), (2012, 2, 15)]
		   andalso dates_in_months([(2011, 1, 10), (2012, 2, 15), (2012, 1, 15)], [3]) = []

val ans6 = get_nth(["ml", "ocaml", "f#"], 1) = "ml"
		   andalso get_nth(["ml", "ocaml", "f#"], 2) = "ocaml"
		   andalso get_nth(["ml", "ocaml", "f#"], 3) = "f#"

val ans7 = date_to_string(2017, 1, 26) = "January 26, 2017"
		   andalso date_to_string(2016, 9, 30) = "September 30, 2016"

val ans8 = number_before_reaching_sum(6, [3, 2, 1, 3]) = 2
		   andalso number_before_reaching_sum(2, [3, 2, 1, 3]) = 0
		   andalso number_before_reaching_sum(10, [3, 2, 1, 3]) = 4

val ans9 = what_month(31) = 1
		   andalso what_month(32) = 2
		   andalso what_month(365) = 12
		   andalso what_month(360) = 12

val ans10 = month_range(30, 32) = [1, 1, 2]
			andalso month_range(1, 5) = [1, 1, 1, 1, 1]
			andalso month_range(1, 1) = [1]
			andalso month_range(5, 1) = []

val ans11 = oldest([(2017, 1, 20)]) =  SOME (2017, 1, 20)
			andalso oldest([(2016, 1, 20), (2016, 12, 12)]) = SOME (2016, 1, 20)
			andalso oldest([(1, 2, 3), (5, 2, 3),(7, 2, 3),(3, 2, 3)]) = SOME (1, 2, 3)
			andalso oldest([]) = NONE