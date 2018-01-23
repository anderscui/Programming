; data types
; primitive: number?

(define atom?
    (lambda  (x)
          (and (not (pair? x)) (not (null? x)))))

; (lambda ...) creates a function;
; (define ...) gives it a name;
; (else ...) asks if else is true which is always true.
(define lat?
  (lambda (l)
    (cond
      ((null? l) #t)
      ((atom? (car l)) (lat? (cdr l)))
      (else #f))))

; list operations.
(define member?
  (lambda (a lat)
    (cond
      ((null? lat) #f)
      ((equal? a (car lat)) #t)
      (else (member? a (cdr lat))))))

(define rember
  (lambda  (a lat)
    (cond
      ((null? lat) (quote ()))
      ((eq? a (car lat)) (cdr lat))
      (else (cons (car lat) (rember a (cdr lat)))))))

(define occur
  (lambda (a lat)
    (cond
      ((null? lat) 0)
      ((= a (car lat)) (add1 (occur a (cdr lat))))
      (else (occur a (cdr lat))))))

(define first
  (lambda (l)
    (car l)))

(define second
  (lambda (l)
    (car (cdr l))))

(define third
  (lambda (l)
    (car (cdr (cdr l)))))

; the nth element of list 'lat'
(define pick
  (lambda (n lat)
    (cond
      ((= n 1) (car lat))
      (else (pick (sub1 n) (cdr lat))))))

; build a list consisting of the two specific items.
(define build
  (lambda (a b)
    (cons a (cons b '()))))

; maths
; is 'n' multiple of 'm', 6 of 3.
(define multiple?
  (lambda (n m)
    (= (remainder n m) 0)))

(define factor?
  (lambda (n m)
    (multiple? m n)))

(define even?
  (lambda (n)
    (= (modulo n 2) 0)))

(define odd?
  (lambda (n)
    (not (even? n))))

; assert
(define eqvals?
  (lambda (v1 v2)
    (if (equal? v1 v2)
      (print "cool")
      (begin (print "oops...") (print v1) (print v2)))))

(define true?
  (lambda (v)
    (if (and (boolean? v) v) (print "cool") (print "oops..."))))

(define false?
  (lambda (v)
    (true? (not v))))

(print "tls.scm loaded, this is the default module.")
(newline)

