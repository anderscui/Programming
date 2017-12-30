(load "tls.scm")

(define set?
  (lambda (lat)
    (cond
      ((null? lat) #t)
      ((member? (car lat) (cdr lat)) #f)
      (else (set? (cdr lat))))))

(false? (set? '(apple 3 pear 4 9 apple 3 4)))
(true? (set? '(apple 3 pear 4 9)))

(define makeset
  (lambda (lat)
    (cond
      [(null? lat) '()]
      [(member? (car lat) (cdr lat)) (makeset (cdr lat))]
      [else (cons (car lat) (makeset (cdr lat)))])))

(eqvals? (makeset '(apple peach pear peach plum apple lemon peach))
         '(pear plum apple lemon peach))

(define subset?
  (lambda (set1 set2)
    (cond
      [(null? set1) #t]
      [(member? (car set1) set2) (subset? (cdr set1) set2)]
      [else #f])))

(true? (subset? '(5 chicken wings) '(5 hamburgers 2 pieces chicken light wings)))


(define eqset?
  (lambda (set1 set2)
    (and (subset? set1 set2) (subset? set2 set1))))

(true? (eqset? '(6 large chickens with wings) '(6 chickens with large wings)))


(define intersect
  (lambda (set1 set2)
    (cond
      [(null? set1) '()]
      [(member? (car set1) set2)
                (cons (car set1) (intersect (cdr set1) set2))]
      [else (intersect (cdr set1) set2)])))


(eqvals? (intersect '(stewed tomatoes and macaroni) '(macaroni and cheese))
         '(and macaroni))


(define union
  (lambda (set1 set2)
    (cond
      [(null? set1) set2]
      [(member? (car set1) set2) (union (cdr set1) set2)]
      [else (cons (car set1) (union (cdr set1) set2))])))

(eqvals? (union '(stewed tomatoes and macaroni casserole) '(macaroni and cheese))
         '(stewed tomatoes casserole macaroni and cheese))
