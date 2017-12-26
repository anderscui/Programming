(load "tls.scm")

; (print (atom? (quote ())))
; (print (atom? 1))

; (print (add1 67))
; (print (sub1 67))

; (print (zero? 0))
; (print (zero? 1))

(define add
  (lambda (a b)
    (cond
      ((zero? b) a)
      (else (add1 (add a (sub1 b)))))))

(print (equal? (add 3 6) 9))


(define sub
  (lambda (a b)
    (cond
      ((zero? b) a)
      (else (sub1 (sub a (sub1 b)))))))

(print (equal? (sub 9 6) 3))

(define tup?
  (lambda (lat)
    (cond
      ((null? lat) #t)
      ((number? (car lat)) (tup? (cdr lat)))
      (else #f))))

(print (tup? '()))
(print (tup? '(1 2 3)))
(print (not (tup? '(3 (7 4) 13 9))))
(print (not (tup? '(1 2 8 'apple 3))))

(define addtup
  (lambda (tup)
    (cond
      ((null? tup) 0)
      (else (+ (car tup) (addtup (cdr tup)))))))

(print (equal? (addtup '(3 5 2 8)) 18))

