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
