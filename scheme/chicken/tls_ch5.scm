(load "tls.scm")

(define rember*
  (lambda (a l)
    (cond
      ((null? l) '())
      ((atom? (car l)) (if (eq? a (car l))
                           (rember* a (cdr l))
                           (cons (car l) (rember* a (cdr l)))))
      (else (cons (rember* a (car l)) (rember* a (cdr l)))))))

(eqvals? (rember* 1 '(1 2 1 2)) '(2 2))
(eqvals? (rember* 'cup '((coffee) cup ((tea) cup) (and (hick)) cup))
         '((coffee) ((tea)) (and (hick))))

(define occur*
  (lambda (a l)
    (cond
      ((null? l) 0)
      ((atom? (car l)) (if (eq? a (car l))
                           (add1 (occur* a (cdr l)))
                           (occur* a (cdr l))))
      (else (+ (occur* a (car l)) (occur* a (cdr l)))))))

(eqvals? (occur* 1 '(1 (((1))))) 2)
(eqvals? (occur* 1 '(1 (2 1) (((1))))) 3)

(define leftmost
  (lambda (l)
    (cond
      ((atom? (car l)) (car l))
      (else (leftmost (car l))))))

(eqvals? (leftmost '(((hot) (tuna (and))) cheese)) 'hot)

