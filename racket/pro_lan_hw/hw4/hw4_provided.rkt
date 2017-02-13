#lang racket

(provide (all-defined-out)) ;; so we can put tests in a second file

;; put your code below
(define (sequence low high stride)
	(if (> low high)
		null
		(cons low (sequence (+ low stride) high stride))))

(define (string-append-map xs suffix)
	(map (lambda (s) (string-append s suffix)) xs))

(define (list-nth-mod xs n)
	(cond [(< n 0) (error "list-nth-mod: negative number")]
		  [(null? xs) (error "list-nth-mod: empty list")]
		  [#t (let ([i (remainder n (length xs))])
		  		(car (list-tail xs i)))]))

(define (stream-for-n-steps s n)
	(if (= n 0)
		null
		(let ([cur (s)])
			(cons (car cur) (stream-for-n-steps (cdr cur) (- n 1))))))


(define funny-number-stream
	(letrec ([f (lambda (x) 
		(if (= (remainder x 5) 0)
			(cons (- x) (lambda () (f (+ x 1))))
			(cons x (lambda () (f (+ x 1))))))])
		(lambda () (f 1))))

(define dan-then-dog
	(letrec ([f (lambda (x) 
				(if (= x 1)
					(cons "dan.jpg" (lambda () (f 0)))
					(cons "dog.jpg" (lambda () (f 1)))))])
		(lambda () (f 1))))

(define (stream-add-zero stream)
	(letrec ([f (lambda (s)
					(let ([cur (s)])
						 (cons (cons 0 (car cur)) (lambda () (f (cdr cur))))))])
		(lambda () (f stream))))

(define (cycle-lists xs ys)
	(letrec ([f (lambda (xi yi)
				(cons (cons (list-nth-mod xs xi) (list-nth-mod ys yi)) (lambda () (f (+ xi 1) (+ yi 1))) ))])
		(lambda () (f 0 0))))

(define (vector-assoc v vec)
	(letrec ([f (lambda (vec v start)
					(cond [(= (vector-length vec) start) #f]
						  [(not (pair? (vector-ref vec start))) (f vec v (+ start 1))]
						  [(equal? v (car (vector-ref vec start))) (vector-ref vec start)]
						  [#t (f vec v (+ start 1))]))])
		(f vec v 0)))

(define (cached-assoc xs n)
	(let ([vs (make-vector n #f)]
		  [next 0])
		(lambda (v)
			(let ([invec (vector-assoc v vs)])
				(if invec
					invec
					(let ([ans (assoc v xs)])
						(if ans
							(begin
								(print "found one")
								(vector-set! vs next ans)
								(set! next (remainder (+ next 1) n))
								ans)
							#f)))))))

; testing helpers
(define nats
	(letrec ([f (lambda (x) (cons x (lambda () (f (+ x 1)))))])
		(lambda () (f 1))))

; sequence
(and (equal? (sequence 3 11 2) (list 3 5 7 9 11))
	 (equal? (sequence 3 8 3) (list 3 6))
	 (equal? (sequence 3 2 1) null))

; string-append-map
(equal? (string-append-map (list "AB " "CD ") "suffix") (list "AB suffix" "CD suffix"))

; list-nth-mod
(and (equal? (list-nth-mod (list 1 2 3 4 5) 0) 1)
	 (equal? (list-nth-mod (list 1 2 3 4 5) 3) 4)
	 (equal? (list-nth-mod (list 1 2 3 4 5) 6) 2))
; (equal? (list-nth-mod (list 1 2 3 4 5) -1) (error "list-nth-mod: negative number"))
; (equal? (list-nth-mod null 1) (error "list-nth-mod: empty list"))

; stream-for-n-steps
(and (equal? (stream-for-n-steps nats 3) (list 1 2 3))
	 (equal? (stream-for-n-steps nats 0) null))

(equal? (stream-for-n-steps funny-number-stream 6) (list 1 2 3 4 -5 6))

(equal? (stream-for-n-steps dan-then-dog 5) (list "dan.jpg" "dog.jpg" "dan.jpg" "dog.jpg" "dan.jpg"))

(equal? (stream-for-n-steps (stream-add-zero dan-then-dog) 3) (list (cons 0 "dan.jpg") (cons 0 "dog.jpg") (cons 0 "dan.jpg")))

(equal? (stream-for-n-steps (cycle-lists (list 1 2 3) (list "a" "b")) 4) (list (cons 1 "a") (cons 2 "b") (cons 3 "a") (cons 1 "b")))

(and (equal? (vector-assoc 3 (vector (cons 1 2) (cons 3 4) "str" (cons 5 6))) (cons 3 4))
	 (equal? (vector-assoc 9 (vector (cons 1 2) (cons 3 4) "str" (cons 5 6))) #f))

(define xlist (list (cons 1 2) (cons 3 4) (cons 5 6) (cons 7 8) (cons 9 10)))
(define cached (cached-assoc xlist 3))

(cached 3)
(cached 3)
(cached 1)
(cached 7)
(cached 9)
(cached 3)
(cached 3)
(cached 5)
(cached 9)
(cached 7)


