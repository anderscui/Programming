(load "tls.scm")

; remove a member by a test? function.
(define rember-test
  (lambda (test? a l)
    (cond
      [(null? l) '()]
      [(test? a (car l)) (cdr l)]
      [else (cons (car l) (rember-test test? a (cdr l)))])))

(eqvals? (rember-test = 5 '(6 2 5 3)) '(6 2 3))
(eqvals? (rember-test eq? 'jelly '(jelly beans are good)) '(beans are good))

; should use equal? instead of eq?
(eqvals? (rember-test equal? '(pop corn) '(lemonade (pop corn) and (cake)))
         '(lemonade and (cake)))

; generate rember function by the 'test?' argument
; here this function is used to generate another one.
(define rember-f
  (lambda (test?)
    (lambda (a l)
      (cond
        [(null? l) '()]
        [(test? a (car l)) (cdr l)]
        [else (cons (car l) ((rember-f test?) a (cdr l)))]))))

(define rember-eq (rember-f eq?))
(eqvals? (rember-eq 1 '(1 2 1 3)) '(2 1 3))

(define multiple?
  (lambda (n m)
    (= (remainder m n) 0)))

(false? (multiple? 3 5))
(true? (multiple? 3 6))

(define rember-multiple (rember-f multiple?))
(eqvals? (rember-multiple 3 '(2 12 3)) '(2 3))

(define insertL-f
  (lambda (test?)
    (lambda (new old l)
      (cond
        [(null? l) '()]
        [(test? old (car l)) (cons new (cons old (cdr l)))]
        [else (cons (car l) ((insertL-f test?) new old (cdr l)))]))))

(define insertR-f
  (lambda (test?)
    (lambda (new old l)
      (cond
        [(null? l) '()]
        [(test? old (car l)) (cons old (cons new (cdr l)))]
        [else (cons (car l) ((insertR-f test?) new old (cdr l)))]))))
