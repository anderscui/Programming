#lang racket

(provide (all-defined-out))


(define-syntax my-if
	(syntax-rules (then else)
		[(my-if e1 then e2 else e3)
		 (if e1 e2 e3)]))

(my-if (> 2 1) then (+ 1 2) else (* 2 3))

(define-syntax comment-out
	(syntax-rules ()
		[(comment-out ignore instead)
		 instead]))

(comment-out (car null) (+ 2 3)) ; no error here.

(define-syntax my-delay
	(syntax-rules ()
		[(my-delay e)
		 (mcons #f (lambda () e))]))

