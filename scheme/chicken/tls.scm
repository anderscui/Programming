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

(define rember
  (lambda  (a lat)
    (cond
      ((null? lat) (quote ()))
      ((eq? a (car lat)) (cdr lat))
      ("otherwise" (cons (car lat) (rember a (cdr lat)))))))

(print "tls.scm loaded, this is the default module.")
(newline)
