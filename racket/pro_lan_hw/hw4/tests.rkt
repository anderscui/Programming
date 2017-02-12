#lang racket

(provide (all-defined-out)) ;; so we can put tests in a second file

(length (list 1 2))
(pair? (cons 1 2))
(vector (cons 1 2) (cons 3 4) "str" (cons 5 6))