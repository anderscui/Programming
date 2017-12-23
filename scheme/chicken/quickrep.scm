(use irregex)

(define (process-line line re rplc)
  (irregex-replace/all re line rplc))

(define (quickrep re rplc)
  (let ((line (read-line)))
    (if (not (eof-object? line))
      (begin
	(display (process-line line re rplc))
	(newline)
	(quickrep re rplc)))))

(define (main args)
  (quickrep (irregex (car args)) (cadr args)))

