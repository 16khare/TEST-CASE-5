import json
import networkx as nx

# Parse the JSON file
with open('build_dag.json') as f:
    modules = json.load(f)

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
for module, data in modules.items():
    G.add_node(module, path=data['path'])  # Add path information to the node
    for dependency in data['dependencies']:
        G.add_edge(dependency['artifactId'], module)

# Perform topological sort
sorted_modules = list(nx.topological_sort(G))

# Print the sorted modules and their paths to a text file
with open('sorted_modules_with_paths.txt', 'w') as f:
    for module in sorted_modules:
        path = G.nodes[module]['path']  # Retrieve the path information for the module
        f.write(f"{module} - Path: {path}\n")

# You can also include additional information like build commands if needed








