#lang racket

(provide (all-defined-out))

(define (slow-add x y)
	(letrec ([slow-id (lambda (y z)
						(if (= 0 z)
							y
							(slow-id y (- z 1))))])
		(+ (slow-id x 9000000) y)))

; (slow-add 5 6)

(define (my-mult x y-thunk)
	(cond [(= x 0) 0]
		  [(= x 1) (y-thunk)]
		  [#t (+ (y-thunk) (my-mult (- x 1) y-thunk))]))

; call slow-add 50 times.
(my-mult 200 (lambda () (slow-add 5 6)))