(load "tls.scm")

(define numbered?
  (lambda (aexp)
    (cond
      ((atom? aexp) (number? aexp))
      (else
        (and (numbered? (car aexp))
             (numbered? (car (cdr (cdr aexp)))))))))

(true? (numbered? 1))
(false? (numbered? 'a))
(true? (numbered? '(1 + 2)))
(true? (numbered? '(1 + (2 * 3))))

(define value
  (lambda (nexp)
    (cond
      ((atom? nexp) nexp)
      ((eq? (second nexp) '+)
        (+ (value (car nexp)) (value (third nexp))))
      ((eq? (car (cdr nexp)) '*)
        (* (value (car nexp)) (value (third nexp))))
      ((eq? (car (cdr nexp)) '^)
        (expt (value (car nexp)) (value (third nexp))))
      (else -1))))

(eqvals? (value '(1 + 2)) 3)
(eqvals? (value '(1 + (3 * 4))) 13)
(eqvals? (value '((1 + 1) ^ (2 * 3))) 64)

; use '() to represent 1.
(define sero?
  (lambda (n)
    (null? n)))

(define edd1
  (lambda (n)
    (cons '() n)))

(define zub1
  (lambda (n)
    (cdr n)))

(define add
  (lambda (n m)
    (cond
      ((sero? m) n)
      (else (edd1 (add n (zub1 m)))))))

(define one '(()))
(define two (edd1 one))
(define three (add one two))
(eqvals? three (edd1 two))
