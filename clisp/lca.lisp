(defstruct node
	key
	left
	right)

(defun get-lca (node n1 n2)
	(if (null node) 
		(return-from get-lca nil))
	(if (or (equal n1 (node-key node)) (equal n2 (node-key node)))
		(return-from get-lca node))
	(let ((left (get-lca (node-left node) n1 n2))
		(right (get-lca (node-right node) n1 n2)))
	(if (and left right)
		(return-from get-lca node)) (or left right)))

(defparameter *root*
	(make-node :key 50))
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

(format t "The LCA of 14 and 19 should be 17, and was found to be ~d~%" (node-key (get-lca *root* 14 19)))