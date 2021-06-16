class Solution:
    

		# we have to initialize ref node
		# do dfs, build neighbor list, using dictionary
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        
        seen = {}  # value: node itself
        
        
        def dfs(node, seen):
            new_node = Node(node.val)
            seen[node.val] = new_node
            new_neighbors = []


            for n in node.neighbors:

                if n.val not in seen:
                    new_neighbors.append(dfs(n, seen))
                else:
                    new_neighbors.append(seen[n.val])

            new_node.neighbors = new_neighbors
            return new_node
    
    
        return dfs(node, seen)
        