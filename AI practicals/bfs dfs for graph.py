# Function to read graph from user
def read_graph():
    graph = {}
    num_edges = int(input("Enter number of edges: "))
    print("Enter each edge in the format: node1 node2")
    for _ in range(num_edges):
        u, v = input().strip().split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)  # Because the graph is undirected
    return graph

# Recursive DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Iterative BFS
def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Main function
def main():
    graph = read_graph()
    start_node = input("Enter starting node: ")

    print("\nDepth First Search (DFS) traversal:")
    dfs(graph, start_node)

    print("\n\nBreadth First Search (BFS) traversal:")
    bfs(graph, start_node)

# Run the main function
main()
