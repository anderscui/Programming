#lang racket

(provide (all-defined-out))

(define mpr (mcons 1 (mcons #t "hi")))

mpr
(pair? mpr) ; #f
(list? mpr) ; #f

(set-mcdr! mpr (mcons #f "good"))
mpr

(set-mcar! (mcdr mpr) "interesting")
mpr