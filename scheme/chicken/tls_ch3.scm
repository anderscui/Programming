(define rember
  (lambda  (a lat)
    (cond
      ((null? lat) lat)
      ((eq? a (car lat)) (cdr lat))
      ("otherwise" (cons (car lat) (rember a (cdr lat)))))))

(print (rember 'mint '(lamb chops and mint jelly)))
(print (rember 'mint '(lamb chops jelly)))
