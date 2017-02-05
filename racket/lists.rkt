#lang racket

(provide (all-defined-out))

(define (sum xs)
	(if (null? xs)
		0
		(+ (car xs) (sum (cdr xs)))))

(print (sum (list 1 2 3 4 5)))
(newline)

; append
(define (my-append xs ys)
	(if (null? xs)
		ys
		(cons (car xs) (my-append (cdr xs) ys))))

(print (my-append (list 1 2 3) (list 4 5 6)))
(newline)

(define (my-map f xs)
	(if (null? xs)
		null
		(cons (f (car xs)) (my-map f (cdr xs)))))

(print (my-map (lambda (x) (+ x 2)) (list 1 2 3)))
(newline)