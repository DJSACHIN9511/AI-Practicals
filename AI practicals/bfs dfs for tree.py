# Function to read a tree from user input
def read_tree():
    tree = {}
    num_nodes = int(input("Enter number of nodes in the tree: "))
    print(f"Enter {num_nodes - 1} edges (format: parent child):")
    for _ in range(num_nodes - 1):
        u, v = input().strip().split()
        if u not in tree:
            tree[u] = []
        if v not in tree:
            tree[v] = []
        tree[u].append(v)
        tree[v].append(u)  # because it's undirected
    return tree

# Recursive DFS for a tree
def dfs(tree, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=' ')
    for child in tree.get(node, []):
        if child not in visited:
            dfs(tree, child, visited)

# Iterative BFS for a tree
def bfs(tree, root):
    visited = set()
    queue = [root]
    visited.add(root)
    while queue:
        current = queue.pop(0)
        print(current, end=' ')
        for child in tree.get(current, []):
            if child not in visited:
                visited.add(child)
                queue.append(child)

# Main function
def main():
    tree = read_tree()
    root = input("Enter root of the tree: ")

    print("\nDFS Traversal of Tree:")
    dfs(tree, root)

    print("\n\nBFS Traversal of Tree:")
    bfs(tree, root)

# Run the main
main()
