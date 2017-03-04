#lang racket

(provide (all-defined-out))

(define (fib x)
	(if (or (= x 1) (= x 2))
		1
		(+ (fib (- x 1))
		   (fib (- x 2)))))

; (fib 30) ; 832040
; (fib 50)

(define (fib2 x)
	(letrec ([f (lambda (acc1 acc2 y)
					(if (= y x)
						(+ acc1 acc2)
						(f (+ acc1 acc2) acc1 (+ y 1))))])
		(if (or (= x 1) (= x 2))
			1
			(f 1 1 3))))

(fib2 50)

(define fib3
	(letrec ([memo null] ; list or pairs (arg . result)
			 [f (lambda (x)
			 		(let ([ans (assoc x memo)])
			 			(if ans
			 				(cdr ans)
			 				(let ([new-ans (if (or (= x 1) (= x 2))
			 								   1
			 								   (+ (f (- x 1))
			 								   	  (f (- x 2))))])
			 					(begin
			 						(set! memo (cons (cons x new-ans) memo))
			 						new-ans)))))])
		f))

(fib3 50)