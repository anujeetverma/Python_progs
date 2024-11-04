import random
from collections import defaultdict

def generate_random_graph(n, num_edges):
    graph = defaultdict(list)
    edges = set()
    
    while len(edges) < num_edges:
        u, v = random.randint(0, n - 1), random.randint(0, n - 1)
        if u != v and (u, v) not in edges and (v, u) not in edges:
            graph[u].append(v)
            graph[v].append(u)
            edges.add((u, v))
    
    return graph

def dfs(u, parent, graph, disc, low, time, stack, components):
    children = 0
    disc[u] = low[u] = time[0]
    time[0] += 1
    for v in graph[u]:
        if disc[v] == -1:
            stack.append((u, v))
            children += 1
            dfs(v, u, graph, disc, low, time, stack, components)
            low[u] = min(low[u], low[v])
            if (parent is None and children > 1) or (parent is not None and low[v] >= disc[u]):
                component = []
                while stack[-1] != (u, v):
                    component.append(stack.pop())
                component.append(stack.pop())
                components.append(component)
        elif v != parent and disc[v] < disc[u]:
            stack.append((u, v))
            low[u] = min(low[u], disc[v])

def find_biconnected_components(graph, n):
    disc = [-1] * n
    low = [-1] * n
    time = [0]
    stack = []
    components = []

    for i in range(n):
        if disc[i] == -1:
            dfs(i, None, graph, disc, low, time, stack, components)

    if stack:
        component = []
        while stack:
            component.append(stack.pop())
        components.append(component)
    
    return components

def main():
    n = int(input("Enter number of vertices: "))
    num_edges = int(input("Enter number of edges: "))
    
    graph = generate_random_graph(n, num_edges)
    
    components = find_biconnected_components(graph, n)
    largest_component = max(components, key=len)
    
    print("Largest Biconnected Component (edges):", largest_component)
    print("Size of Largest Biconnected Component:", len(largest_component))

main()