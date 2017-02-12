#lang racket

(provide (all-defined-out))

(define (my-if-strange e1 e2 e3)
	(if e1 (e2) (e3)))

(define (factorial x)
	(my-if-strange
		(= x 0)
		(lambda () 1)
		(lambda () (* x (factorial (- x 1))))))

(factorial 5)
(factorial 500)