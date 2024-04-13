import json
import networkx as nx

# Parse the JSON file
with open('build_dag.json') as f:
    modules = json.load(f)

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
for module, data in modules.items():
    # Ensure 'path' attribute is set for each node, default to empty string if not provided
    path = data.get('path', '')
    G.add_node(module, path=path)
    for dependency in data['dependencies']:
        G.add_edge(dependency['artifactId'], module)

# Perform topological sort on the graph
sorted_modules = list(nx.topological_sort(G))

# Create a list of tuples containing the sorted modules and their path information
# Safely access 'path' attribute, providing a default value if it doesn't exist
sorted_modules_with_paths = [(module, G.nodes[module].get('path', 'Path not found')) for module in sorted_modules]

# Print the sorted modules and their paths to a text file
with open('sorted_modules_with_paths.txt', 'w') as f:
    for module, path in sorted_modules_with_paths:
        f.write(f"{module} - Path: {path}\n")






