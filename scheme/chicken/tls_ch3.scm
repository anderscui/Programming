(define rember
  (lambda  (a lat)
    (cond
      ((null? lat) (quote ()))
      ((eq? a (car lat)) (cdr lat))
      ("otherwise" (cons (car lat) (rember a (cdr lat)))))))

; don't use eq? or eqv?
(print (equal? (rember 'mint '(lamb chops and mint jelly)) '(lamb chops and jelly)))
(print (equal? (rember 'mint '(lamb chops jelly)) '(lamb chops jelly)))
(print (equal? (rember 'sauce '(soy sauce and tomato sauce)) '(soy and tomato sauce)))

(define firsts
  (lambda  (lists)
    (cond
      ((null? lists) (quote ()))
      ("otherwise" (cons (car (car lists)) (firsts (cdr lists)))))))

(print (equal? (firsts '((a b) (c d) (e f))) '(a c e)))

(define insertR
  (lambda (new old lat)
    (cond
      ((null? lat) (quote ()))
      ((eq? old (car lat)) (cons old (cons new (cdr lat))))
      ("otherwise" (cons (car lat) (insertR new old (cdr lat)))))))

(print (equal?
  (insertR 'topping 'fudge '(ice cream with fudge for dessert))
  '(ice cream with fudge topping for dessert)))


(define insertL
  (lambda (new old lat)
    (cond
      ((null? lat) (quote ()))
      ((eq? old (car lat)) (cons new lat))
      ("otherwise" (cons (car lat) (insertL new old (cdr lat)))))))

(print (equal? (insertL 'c 'd '(a b d e)) '(a b c d e)))

(define subst2
  (lambda (new o1 o2 lat)
    (cond
      ((null? lat) (quote ()))
      ((or (eq? o1 (car lat)) (eq? o2 (car lat))) (cons new (cdr lat)))
      (else (cons (car lat) (subst2 new o1 o2 (cdr lat)))))))

(print (equal? (subst2 'vanilla 'chocolate 'banana '(banana ice cream with chocolate topping))
               '(vanilla ice cream with chocolate topping)))

; remove all occurrences
(define multirember
  (lambda  (a lat)
    (cond
      ((null? lat) (quote ()))
      ((eq? a (car lat)) (multirember a (cdr lat)))
      (else (cons (car lat) (multirember a (cdr lat)))))))

; don't use eq? or eqv?
(print (equal? (multirember 'mint '(lamb mint chops and mint jelly)) '(lamb chops and jelly)))

; substitute all occurrences
(define multisubst
  (lambda (new old lat)
    (cond
      ((null? lat) (quote ()))
      ((eq? old (car lat)) (cons new (multisubst new old (cdr lat))))
      (else (cons (car lat) (multisubst new old (cdr lat)))))))

(print (equal? (multisubst 'b 'd '(a d c d e)) '(a b c b e)))

