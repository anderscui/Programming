#lang racket

(provide (all-defined-out))

(= (if 1 2 3) 2)
(= (if null 2 3) 2)
(= (if "false" 2 3) 2)
(= (if #f 2 3) 3)

(define (count-falses xs)
	(cond [(null? xs) 0]
		  [(car xs) (count-falses (cdr xs))]
		  ["otherwise" (+ 1 (count-falses (cdr xs)))]))

(= (count-falses (list #t #f 1 2 #f)) 2)