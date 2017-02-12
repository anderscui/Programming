#lang racket

(provide (all-defined-out))

(define xs (list 4 5 6))
(define ys (list (list 4 5) 6 7 (list 8) 9 2 3 (list 0 1)))
; ys

(define (sum1 xs)
	(if (null? xs)
		0
		(if (number? (car xs))
			(+ (car xs) (sum1 (cdr xs)))
			(+ (sum1 (car xs)) (sum1 (cdr xs))))))

(sum1 xs)
(sum1 ys)