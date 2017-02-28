#lang racket

(provide (all-defined-out))

(struct obj (fields methods) #:transparent)

(define (assoc-m v xs)
	(cond [(null? xs) #f]
		  [(equal? v (mcar (car xs))) (car xs)]
		  [#t (assoc-m v (cdr xs))]))

(define (get obj fld)
	(let ([pr (assoc-m fld (obj-fields obj))])
		(if pr
			(mcdr pr)
			(error "field not found"))))

(define (set obj fld v)
	(let ([pr (assoc-m fld (obj-fields obj))])
		(if pr
			(set-mcdr! pr v)
			(error "field not found"))))

(define (send obj msg . args)
	(let ([pr (assoc msg (obj-methods obj))])
		(if pr
			((cdr pr) obj args)
			(error "method not found" msg))))

(define (make-point _x _y)
	(obj
		(list (mcons 'x _x)
			  (mcons 'y _y))
		(list (cons 'get-x (lambda (self args) (get self 'x)))
			  (cons 'get-y (lambda (self args) (get self 'y)))
			  (cons 'set-x (lambda (self args) (set self 'x (car args))))
			  (cons 'set-y (lambda (self args) (set self 'y (car args))))
			  (cons 'distToOrigin
			  	(lambda (self args)
			  		(let ([a (send self 'get-x)]
			  			  [b (send self 'get-y)])
			  			(sqrt (+ (* a a) (* b b)))))))))

(define p1 (make-point 3 4))
; p1	
(send p1 'get-x)
(send p1 'get-y)
(send p1 'distToOrigin)
























