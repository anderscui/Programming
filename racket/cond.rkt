#lang racket

(provide (all-defined-out))

(define xs (list 4 5 6))
(define ys (list (list 4 5) 6 7 (list 8) 9 2 3 (list 0 1)))
; ys

(define (sum1 xs)
	(cond [(null? xs) 0]
		  [(number? (car xs)) (+ (car xs) (sum1 (cdr xs)))]
		  [#t (+ (sum1 (car xs)) (sum1 (cdr xs)))]))

; test cases
(= (sum1 xs) 15)
(= (sum1 ys) 45)