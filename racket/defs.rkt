#lang racket

(provide (all-defined-out))

(define x 3) ; val x = 3
(define y (+ x 2))

; lambda: anonymous function
(define cube1
	(lambda (x)
		(* x (* x x))))

(define cube2
	(lambda (x)
		(* x x x)))

; syntactic sugar of above
(define (cube3 x)
	(* x x x))

(print (cube3 3))
(newline)

(define (pow1 x y)
	(if [= y 0]
		1
		(* x (pow1 x (- y 1)))))

; currying
(define pow2
	(lambda (x)
		(lambda (y)
			(pow1 x y))))

(define three-to-the (pow2 3))
(print three-to-the)
(newline)
(print (three-to-the 2))
(newline)