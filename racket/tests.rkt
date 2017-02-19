#lang racket

(provide (all-defined-out)) ;; so we can put tests in a second file

; (length (list 1 2))
; (pair? (cons 1 2))
; (vector (cons 1 2) (cons 3 4) "str" (cons 5 6))

(cadr (list 1 2))
(caddr (list 1 2 3))

(pair? (list 1 2))
(pair? null)

(define (sum lst)
	(if (pair? lst)
		(+ (car lst) (sum (cdr lst)))
		0))
(sum null)
(sum (list 1 2 3))