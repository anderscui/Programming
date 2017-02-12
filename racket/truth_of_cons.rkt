#lang racket

(provide (all-defined-out))

(define pr (cons 1 (cons #t "hi"))) ; a pair
(define lst (cons 1 (cons #t (cons "hi" null)))) ; a list, a special pair ending with "null"

; pr
; lst
(string=? (cdr (cdr pr)) "hi") ; ans: "hi" => cdr is like #2 in ML
(string=? (car (cdr (cdr lst))) "hi") ; cdr of list => list

(pair? pr)
(pair? lst)

(list? pr)
(list? lst)