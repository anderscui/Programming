(load "tls.scm")

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

(define tup?
  (lambda (l)
    (cond
      ((null? l) #t)
      ((number? (car l)) (tup? (cdr l)))
      (else #f))))

(true? (tup? '()))
(true? (tup? '(1 2 3)))
(true? (not (tup? '(1 (1 2) 3))))

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

(define len
  (lambda (lat)
    (cond
      ((null? lat) 0)
      (else (add1 (len (cdr lat)))))))

(eqvals? (len '(ham and cheese on rye)) 5)

(define pick
  (lambda (n lat)
    (cond
      ((= n 1) (car lat))
      (else (pick (sub1 n) (cdr lat))))))

(eqvals? (pick 4 '(lasagna spaghetti ravioli macaroni meatball)) 'macaroni)

