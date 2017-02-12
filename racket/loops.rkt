#lang racket

(provide (all-defined-out))

(define-syntax my-let*
	(syntax-rules ()
		[(my-let* () body)
		 body]
		[(my-let* ([var0 val0]
				   [var-rest val-rest] ...)
					body)
			(let ([var0 val0])
				(my-let* ([var-rest val-rest] ...)
						   body))]))

(my-let* () (+ 1 1))
(my-let* ([x 1]) (+ x x))
(my-let* ([x 1]
		  [y 2]) (+ x y))
(my-let* ([x 1]
		  [y 2]
		  [z 3]) (+ x y z))

(define-syntax for
	(syntax-rules (to do)
		[(for lo to hi do body)
		 (let ([l lo]
		 	   [h hi])
		 	(letrec ([loop (lambda (it)
		 						(if (> it h)
		 							#t
		 							(begin body (loop (+ it 1)))))])
		 		(loop l)))]))

(for 7 to 11 do (print "hi"))

(define (f x) (begin (print "A") x))
(define (g x) (begin (print "B") x))
(define (h x) (begin (print "C") x))
(for (f 7) to (g 11) do (h 9))

(define-syntax let2
	(syntax-rules ()
		[(let2 () body)
		 body]
		[(let2 (var val) body)
		 (let ([var val]) body)]
		[(let2 (var1 val1 var2 val2) body)
		 (let ([var1 val1])
		 	(let ([var2 val2])
		 		body))]))

(let2 (x 1 y 2) (+ x y))
(let2 (x 1) (+  x x))
(let2 () (+ 2 2))



