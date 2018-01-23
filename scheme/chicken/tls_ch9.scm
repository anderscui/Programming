(load "tls.scm")

(eqvals? (pick 2 '(1 2 3)) 2)


(define keep-looking
  (lambda (a index lat)
    (cond
      [(equal? (pick index lat) a) #t]
      [(number? (pick index lat)) (keep-looking a (pick index lat) lat)]
      [else #f])))

; assume 'a' is not a number.
(define keep-looking
  (lambda (a sorn lat)
    (cond
      [(number? sorn) (keep-looking a (pick sorn lat) lat)]
      [else (equal? sorn a)])))

(define looking
  (lambda (a lat)
    (keep-looking a (pick 1 lat) lat)))

(false? (looking 'caviar '(6 2 grits caviar 5 7 3)))
(true? (looking 'caviar '(6 2 4 caviar 5 7 3)))

(define build
  (lambda (a b)
    (cons a (cons b '()))))

(define shift
  (lambda (pair)
    (build (first (first pair)) (build (second (first pair)) (second pair)))))

(eqvals? (shift '((a b) (c d))) '(a (b (c d))))

(define align
  (lambda (pora)
    (cond
      [(atom? pora) pora]
      [(pair? (first pora)) (align (shift pora))]
      [else (build (first pora) (align (second pora)))])))

