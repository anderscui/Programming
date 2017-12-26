; (load "tls.scm")
(atom? (quote ()))
(atom? 1)

(atom? '(atom)) ; #t
(list? '(atom turkey or)) ; #t
(list? '((atom turkey) or))
(list? '()) ; #t

(car '(a b c)) ; a

(cons 'peanut '(butter and jelly)) ; (peanut butter and jelly)
