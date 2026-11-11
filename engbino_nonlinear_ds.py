from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_bfs(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def tree_dfs_preorder(root):
    if not root:
        return []
    return [root.val] + tree_dfs_preorder(root.left) + tree_dfs_preorder(root.right)

def tree_dfs_inorder(root):
    if not root:
        return []
    return tree_dfs_inorder(root.left) + [root.val] + tree_dfs_inorder(root.right)

def tree_dfs_postorder(root):
    if not root:
        return []
    return tree_dfs_postorder(root.left) + tree_dfs_postorder(root.right) + [root.val]

root = TreeNode('E')
root.left = TreeNode('N')
root.right = TreeNode('G')
root.left.left = TreeNode('B')
root.left.right = TreeNode('I')
root.right.left = TreeNode('N')
root.right.right = TreeNode('O')

print("==========================================")
print("       PART 1: BINARY TREE (ENGBINO)")
print("==========================================")
print("BFS (Level-Order):", " -> ".join(tree_bfs(root)))
print("DFS Pre-order:    ", " -> ".join(tree_dfs_preorder(root)))
print("DFS In-order:     ", " -> ".join(tree_dfs_inorder(root)))
print("DFS Post-order:   ", " -> ".join(tree_dfs_postorder(root)))

graph = {
    'E':  ['B', 'N1'],
    'N1': ['E', 'G', 'I'],
    'G':  ['N1', 'N2'],
    'B':  ['E', 'I'],
    'I':  ['B', 'N1', 'N2'],
    'N2': ['G', 'I', 'O'],
    'O':  ['N2']
}

def graph_bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in sorted(graph[vertex]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

def graph_dfs(graph, start, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []
    visited.add(start)
    result.append(start)
    for neighbor in sorted(graph[start]):
        if neighbor not in visited:
            graph_dfs(graph, neighbor, visited, result)
    return result

print("\n==========================================")
print("         PART 2: GRAPH (ENGBINO)")
print("==========================================")
print("BFS:", " -> ".join(graph_bfs(graph, 'E')))
print("DFS:", " -> ".join(graph_dfs(graph, 'E')))
