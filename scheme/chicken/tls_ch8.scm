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

(define seqL
  (lambda (new old l)
    (cons new (cons old l))))

(define seqR
  (lambda (new old l)
    (cons old (cons new l))))

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

(define insert-g
  (lambda (seq)
    (lambda (new old l)
      (cond
        [(null? l) '()]
        [(equal? old (car l)) (seq new old (cdr l))]
        [else (cons (car l) ((insert-g seq) new old (cdr l)))]))))

; use an anonymous function to create a new function
(define insertL
  (insert-g
    (lambda (new old l)
      (cons new (cons old l)))))

(define atom-to-func
  (lambda (x)
    (cond
      [(equal? x '+) +]
      [(equal? x '*) *]
      [(equal? x '^) expt])))

(define value
  (lambda (nexp)
    (cond
      ((atom? nexp) nexp)
      (else ((atom-to-func (car (cdr nexp)))
              (value (car nexp))
              (value (third nexp)))))))

(eqvals? (value '(1 + 2)) 3)
(eqvals? (value '(1 + (3 * 4))) 13)
(eqvals? (value '((1 + 1) ^ (2 * 3))) 64)

(define eq?-c
  (lambda (a)
    (lambda (x)
      (equal? x a))))

; define a function to check a single item.
(define eq?-tuna (eq?-c 'tuna))

; remove all items which meet the specific predicate.
(define multiremberT
  (lambda (test? lat)
    (cond
      [(null? lat) '()]
      [(test? (car lat)) (multiremberT test? (cdr lat))]
      [else (cons (car lat) (multiremberT test? (cdr lat)))])))

(eqvals? (multiremberT eq?-tuna '(shrimp salad tuna salad and tuna))
         '(shrimp salad salad and))

; start of continuation
(define multirember&co
  (lambda (a lat col)
    (cond
      [(null? lat) (col '() '())]
      [(equal? a (car lat))
        (multirember&co a (cdr lat)
          (lambda (newlat seen)
            (col newlat
              (cons (car lat) seen))))]
      [else (multirember&co a (cdr lat)
          (lambda (newlat seen)
            (col (cons (car lat) newlat) seen)))])))

; a simple collector
(define a-friend
  (lambda (x y)
    (null? y)))

(false? (multirember&co 'tuna '(strawberries tuna and swordfish) a-friend))
(true? (multirember&co 'tuna '() a-friend))
(false? (multirember&co 'tuna '(tuna) a-friend))

; see, the final result depends on 'col' and ternimal exp, e.g. (col '() '()).
; the final call: (col (atoms not equal to a) (atoms equal to a))
(define how-many-others
  (lambda (x y)
    (length x)))

; there are 3 atoms that are not equal to 'tuna
(eqvals? (multirember&co 'tuna '(strawberries tuna and swordfish) how-many-others) 3)

