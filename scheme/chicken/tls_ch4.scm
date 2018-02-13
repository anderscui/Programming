(load "tls.scm")

(eqvals? (add1 67) 68)
(eqvals? (sub1 67) 66)

(true? (zero? 0))
(false? (zero? 1))

(define add
	(lambda (n m)
		(cond
			((zero? m) n)
			(else (add1 (add n (sub1 m)))))))

(define sub
	(lambda (n m)
		(cond
			((zero? m) n)
			(else (sub1 (sub n (sub1 m)))))))

(eqvals? (add 3 6) 9)
(eqvals? (sub 9 6) 3)

; is l a list of numbers.
(define tup?
  (lambda (l)
    (cond
      ((null? l) #t)
      ((number? (car l)) (tup? (cdr l)))
      (else #f))))

(true? (tup? '()))
(true? (tup? '(1 2 3)))
(false? (tup? '(1 (1 2) 3)))
(false? (tup? '(3 (7 4) 13 9)))
(false? (tup? '(1 2 8 'apple 3)))

; sum a tuple.
(define addtup
  (lambda (tup)
    (cond
      ((null? tup) 0)
      (else (+ (car tup) (addtup (cdr tup)))))))

(eqvals? 18 (addtup '(3 5 2 8)))

(define times
  (lambda (n m)
    (cond
      ((zero? m) 0)
      (else (+ n (times n (sub1 m)))))))

(eqvals? (times 3 6) 18)

(define tup+
  (lambda (tup1 tup2)
    (cond
      ((null? tup1) tup2)
      ((null? tup2) tup1)
      (else (cons (+ (car tup1) (car tup2)) (tup+ (cdr tup1) (cdr tup2)))))))

(eqvals? (tup+ '(3 6 9 11 4) '(8 5 2 0 7)) '(11 11 11 11 11))
(eqvals? (tup+ '(3 7 8 1) '(4 6)) '(7 13 8 1))

(define gt
  (lambda (n m)
    (cond
      ((zero? n) #f)
      ((zero? m) #t)
      (else (gt (sub1 n) (sub1 m))))))

(false? (gt 3 3))
(false? (gt 1 2))
(true? (gt 9 6))

(define exp
  (lambda (n m)
    (cond
      ((zero? m) 1)
      (else (* n (exp n (sub1 m)))))))

(eqvals? (exp 2 3) 8)

(define div
  (lambda (n m)
    (cond
      ((< n m) 0)
      (else (add1 (div (- n m) m))))))

(eqvals? (div 7 3) 2)

(eqvals? (len '(ham and cheese on rye)) 5)

(eqvals? (nth 4 '(lasagna spaghetti ravioli macaroni meatball)) 'macaroni)

(define no-nums
  (lambda (lat)
    (cond
      ((null? lat) '())
      ((number? (car lat)) (no-nums (cdr lat)))
      (else (cons (car lat) (no-nums (cdr lat)))))))

(eqvals? (no-nums '(5 pears 6 prunes 9 dates)) '(pears prunes dates))

(eqvals? (occur 1 '(1 2 1 2 3)) 2)
(eqvals? (occur 10 '(1 2 1 2 3)) 0)
