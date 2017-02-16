#lang racket

(provide (all-defined-out)) ;; so we can put tests in a second file

(struct foo (bar baz quux) #:transparent)

(define foo1 (foo 1 2 3))

; introduces several functions
(foo? foo1)
; (foo? (list 1 2 3)) ; #f

(list (foo-bar foo1) (foo-baz foo1) (foo-quux foo1))

; expressions
(struct const (int) #:transparent)
(struct negate (e) #:transparent)
(struct add (e1 e2) #:transparent)
(struct multiply (e1 e2) #:transparent)

(define (eval-exp e)
	(cond [(const? e) e]
		  [(negate? e) (const (- (const-int (eval-exp (negate-e e)))))]
		  [(add? e) (let ([v1 (const-int (eval-exp (add-e1 e)))]
		  				  [v2 (const-int (eval-exp (add-e2 e)))])
		  				(const (+ v1 v2)))]
		  [(multiply? e) (let ([v1 (const-int (eval-exp (multiply-e1 e)))]
		  				  [v2 (const-int (eval-exp (multiply-e2 e)))])
		  				(const (* v1 v2)))]
		  [#t (error "eval-exp expected an exp")]))

(eval-exp (const 1))
(eval-exp (negate (const 1)))
(eval-exp (multiply (add (const 1) (const 2)) (add (const 3) (const 4))))
