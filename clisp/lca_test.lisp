(load "lca")
(load "lisp-unit")
(use-package :lisp-unit)
(setq *print-failures* t)

(defparameter *root*
	(make-node :key 50))

(define-test test-lca-nil
	(assert-nil (get-lca *root* 14 19)))

(define-test test-lca-valid
	(setf (node-left *root*) (make-node :key 17))
	(setf (node-left(node-left *root*)) (make-node :key 9))
	(setf (node-right (node-left(node-left *root*))) (make-node :key 14))
	(setf (node-left (node-right (node-left(node-left *root*)))) (make-node :key 12))
	(setf (node-right (node-left *root*)) (make-node :key 23))
	(setf (node-left (node-right (node-left *root*))) (make-node :key 19))
	(setf (node-right *root*) (make-node :key 76))
	(setf (node-left (node-right *root*)) (make-node :key 54))
	(setf (node-right (node-left (node-right *root*))) (make-node :key 72))
	(setf (node-left (node-right (node-left (node-right *root*)))) (make-node :key 67))
	(assert-equal 17 (node-key (get-lca *root* 14 19))))

(run-tests :all)