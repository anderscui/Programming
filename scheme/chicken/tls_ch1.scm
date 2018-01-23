(load "tls.scm")

(false? (atom? (quote ())))
(true? (atom? 1))

(false? (atom? '(atom)))
(true? (list? '(atom turkey or)))
(true? (list? '((atom turkey) or)))
(true? (list? '()))

(eqvals? (car '(a b c)) 'a)

(eqvals? (cons 'peanut '(butter and jelly)) '(peanut butter and jelly))
