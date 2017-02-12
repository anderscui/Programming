#lang racket

(provide (all-defined-out))

(define b 3)

(define f
	(let ([b b]) ; make a local copy to avoid outside mutations
		(lambda (x) (* 1 (+ x b)))))
