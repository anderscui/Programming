#lang racket

(provide (all-defined-out))

(define (slow-add x y)
	(letrec ([slow-id (lambda (y z)
						(if (= 0 z)
							y
							(slow-id y (- z 1))))])
		(+ (slow-id x 90000000) y)))

(define (my-mult x y-thunk)
	(cond [(= x 0) 0]
		  [(= x 1) (y-thunk)]
		  [#t (+ (y-thunk) (my-mult (- x 1) y-thunk))]))


(define (my-delay th)
	(mcons #f th))

; use closure, mutation to implement lazy eval.
(define (my-force p)
	(if (mcar p) ; if evaluated?
		(mcdr p)
		(begin (set-mcar! p #t)
			   (set-mcdr! p ((mcdr p)))
			   (mcdr p))))

(my-mult 200 (let ([p (my-delay (lambda () (slow-add 5 6)))])
				(lambda () (my-force p))))

