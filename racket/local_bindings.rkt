#lang racket

(provide (all-defined-out))

; lets
; 1. let
; 2. let*
; 3. letrec
; 4. define

(define (max-of-list xs)
	(cond [(null? xs) (error "max-of-list given empty list")] ; empty list
		  [(null? (cdr xs)) (car xs)] ; one element
		  ["at least 2" (let ([max-of-tl (max-of-list (cdr xs))])
		  	  				 (if (> (car xs) max-of-tl)
		  	  				 	 (car xs)
		  	  				 	 max-of-tl))]))

(= (max-of-list (list 3 2 5 8 6)) 8)
; (max-of-list null)