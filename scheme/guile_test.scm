#!/usr/local/bin/guile -s
!#
(system "echo test")
(newline)

(define (test x) (+ x 1))
(write (test 2))

(define (test2 lst)
	(if (lst)
	0
	(+ 1 (test2 (cdr lst)))))
(test2 (system "ls *.txt"))

