#lang racket

(provide (all-defined-out)) ;; so we can put tests in a second file

; expressions
(struct const (int) #:transparent)
(struct negate (e1) #:transparent)
(struct add (e1 e2) #:transparent)
(struct multiply (e1 e2) #:transparent)
(struct bool (b) #:transparent)
(struct eq-num (e1 e2) #:transparent)
(struct if-then-else (e1 e2 e3) #:transparent)

(define (eval-exp e)
	(cond [(const? e) e]
		  [(negate? e)
		   (let ([v (eval-exp (negate-e1 e))])
		   		(if (const? v)
		   			(const (- (const-int v)))
		   			(error "negate applied to non-number")))]
		  [(add? e) 
		   (let ([v1 (eval-exp (add-e1 e))]
		  		 [v2 (eval-exp (add-e2 e))])
		   		(if (and (const? v1) (const? v2))
		  			(const (+ (const-int v1) (const-int v2)))
		  			(error "add applied to non-number")))]
		  [(multiply? e) 
		   (let ([v1 (eval-exp (multiply-e1 e))]
		  		 [v2 (eval-exp (multiply-e2 e))])
		  		(if (and (const? v1) (const? v2))
		  			(const (* (const-int v1) (const-int v2)))
		  			(error "multiply applied to non-number")))]
		  [(bool? e) e]
		  [(eq-num? e)
		   (let ([v1 (eval-exp (eq-num-e1 e))]
		   		 [v2 (eval-exp (eq-num-e2 e))])
		   	  (if (and (const? v1) (const? v2))
		   	  	  (bool (= (const-int v1) (const-int v2)))
		   	  	  (error "eq-num applied to non-number")))]
		  [(if-then-else? e)
		   (let ([v-test (eval-exp (if-then-else-e1 e))])
		   	  (if (bool? v-test)
		   	  	  (if (bool-b v-test)
		   	  	  	  (eval-exp (if-then-else-e2 e))
		   	  	  	  (eval-exp (if-then-else-e3 e)))
		   	  	  (error "if-then-else applied to non-boolean")))]
		  [#t (error "eval-exp expected an exp")]))

(define (andalso e1 e2)
	(if-then-else e1 e2 (bool #f)))

(define (double e)
	(multiply e (const 2)))

(define (list-product es)
	(if (null? es)
		(const 1)
		(multiply (car es) (list-product (cdr es)))))

(define test (andalso (eq-num (double (const 4))
							  (list-product (list (const 2)
							  					  (const 2)
							  					  (const 1)
							  					  (const 2))))
					  (bool #t)))

(eval-exp (const 1))
(eval-exp (negate (const 1)))
(eval-exp (multiply (add (const 1) (const 2)) (add (const 3) (const 4))))
(eval-exp (bool #t))
(eval-exp (eq-num (const 3) (add (const 1) (const 2))))
(eval-exp (if-then-else (eq-num (const 3) (add (const 1) (const 2)))
						(multiply (const 2) (const 3))
						(const 2)))

(eval-exp (andalso (bool #t) (eq-num (const 1) (const 2))))

(eval-exp test)

