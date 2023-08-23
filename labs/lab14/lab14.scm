(define (split-at lst n)
  'YOUR-CODE-HERE
  (if (null? lst)
      (cons nil nil)
      (if (> n 0)
          (cons (cons (car lst) (car (split-at (cdr lst) (- n 1)))) (cdr (split-at (cdr lst) (- n 1))))
          (cons nil (cons (car lst) (cdr (split-at (cdr lst) (- n 1)))))
          )
        )
)


(define (compose-all funcs)
  'YOUR-CODE-HERE
  (define (helper x)
      (if (null? funcs)
          x
          ((compose-all (cdr funcs)) ((car funcs) x)))
      )
  helper
)

