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

(define member?
  (lambda (a lat)
    (cond
      ((null? lat) #f)
      ((eq? a (car lat)) #t)
      ("so let's go on" (member? a (cdr lat))))))

(define member2?
  (lambda (a lat)
    (cond
      ((null? lat) #f)
      (else (or (eq? a (car lat))
                (member? a (cdr lat)))))))

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
