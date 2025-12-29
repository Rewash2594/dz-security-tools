import yaml
import networkx as nx
import sys

def load_input(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def build_graph(data):
    graph = nx.DiGraph()

    for identity in data.get("identities", []):
        for key, value in identity.items():
            if isinstance(value, list):
                for v in value:
                    graph.add_edge(key, v)
            else:
                graph.add_edge(key, value)

    for trust in data.get("trust", []):
        graph.add_edge(trust["from"], trust["to"])

    return graph

def find_paths(graph):
    roots = [n for n in graph.nodes if graph.in_degree(n) == 0]
    paths = []

    for root in roots:
        for target in graph.nodes:
            if root != target:
                for path in nx.all_simple_paths(graph, root, target):
                    if len(path) > 1:
                        paths.append(path)
    return paths

def main():
    if len(sys.argv) != 2:
        print("Usage: python graph_builder.py <input.yaml>")
        sys.exit(1)

    data = load_input(sys.argv[1])
    graph = build_graph(data)
    paths = find_paths(graph)

    if not paths:
        print("No authority paths found.")
        return

    print("\nDiscovered authority paths:\n")
    for path in paths:
        print(" → ".join(path))

if __name__ == "__main__":
    main()
