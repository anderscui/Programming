#lang racket

(provide (all-defined-out))


(define ones
	(lambda () (cons 1 ones)))

; (car (ones))
; (car ((cdr (ones))))

; (define (f start) (cons start (f (+ start 1))))

; (define nats
; 	(letrec ([f (lambda (x) (cons x (lambda () (f (+ x 1)))))])
; 		(lambda () (f 1))))

(define (make-stream next-val start)
	(letrec ([f (lambda (x) (cons x (lambda () (f (next-val x)))))])
		(lambda () (f start))))

(define nats (make-stream (lambda (x) (+ x 1)) 1))

(car (nats))
(car ((cdr (nats))))
(car ((cdr ((cdr (nats))))))
(newline)

(define power-of-two (make-stream (lambda (x) (* x 2)) 2))

(car (power-of-two))
(car ((cdr (power-of-two))))
(car ((cdr ((cdr (power-of-two))))))