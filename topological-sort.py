import json
import networkx as nx

# Parse the JSON file
with open('build_dag.json') as f:
    modules = json.load(f)

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
order = []
for module, data in modules.items():
    G.add_node(module, path=data.get('path', ''))  # Add path information to the node, default to empty string if 'path' is missing
    for dependency in data['dependencies']:
        G.add_edge(dependency['artifactId'], module)
    order.append(module)

# Sort nodes based on the custom order
sorted_nodes = [node for node in order if node in G]

# Perform topological sort on the sorted nodes
sorted_modules = list(nx.topological_sort(G.subgraph(sorted_nodes)))

# Create a list of tuples containing the sorted modules and their path information
sorted_modules_with_paths = [(module, G.nodes[module]['path']) for module in sorted_modules]

# Print the sorted modules and their paths to a text file
with open('sorted_modules_with_paths.txt', 'a') as f:
    for module, path in sorted_modules_with_paths:
        f.write(f"{module} - Path: {path}\n")

# You can also include additional information like build commands if needed







