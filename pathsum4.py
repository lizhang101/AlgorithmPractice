"""
Given a list of ascending three-digits integers representing a binary with the depth smaller than 5. You need to return the sum of all paths from the root towards the leaves.
If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.
For each integer in this list:
The hundreds digit represents the depth D of this node, 1 <= D <= 4.
The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
The units digit represents the value V of this node, 0 <= V <= 9.

Input: [113, 215, 221]
Output: 12
Explanation:
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.

Input: [113, 221]
Output: 4
Explanation:
The tree that the list represents is:
    3
     \
      1

The path sum is (3 + 1) = 4.
"""

def path_sum(list_tree):
	"""
	solution 1. rebuild the tree.
	solution 2. the tree is small. just alloc a list that can hold all the nodes of a complete binary tree with 5 levels.
				To save the space, we can just use a hash.
	solution 3. do in-place update.
	
	Implemented solution 2.
	:param tree: the list for the tree nodes.
	:return: return the path sum
	"""
	def parse(n):
		rtn = [0] * 3
		for i in range(3):
			rtn[i] = n % 10
			n //= 10
		return rtn

	#build the tree
	tree_map = {}
	for n in list_tree:
		v, p, d = parse(n)
		tree_map[(d,p)] = v
	print (tree_map)
	
	# now traverse the tree
	def traverse(d, p, tree_map):
		if (d, p) not in tree_map:
			return 0
		
		s = 0
		left = traverse(d+1, 2**p - 1, tree_map);
		right = traverse(d+1, 2**p, tree_map);
		
		if left == 0 and right == 0:
			return tree_map[(d,p)]
		
		if left != 0:
			s += tree_map[(d,p)] + left
			
		if right != 0:
			s += tree_map[(d,p)] + right
		return s
	
	return traverse(1, 1, tree_map)

input = [113, 215, 221]
print(path_sum(input))
	
	
	
	
	
	
	
	

