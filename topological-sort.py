import json
import networkx as nx

# Parse the JSON file
with open('build_dag.json') as f:
    modules = json.load(f)

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
for module, data in modules.items():
    # Add node with path information
    G.add_node(module, path=data.get('path', '')) # Default to empty string if 'path' is missing
    # Add edges for dependencies
    for dependency in data['dependencies']:
        G.add_edge(dependency['artifactId'], module)

# Perform topological sort on the graph
# This step ensures that the modules are sorted in a way that dependencies are built before the modules that depend on them
sorted_modules = list(nx.topological_sort(G))

# Create a list of tuples containing the sorted modules and their path information
sorted_modules_with_paths = [(module, G.nodes[module]['path']) for module in sorted_modules]

# Print the sorted modules and their paths to a text file
with open('sorted_modules_with_paths.txt', 'w') as f: # Use 'w' mode to overwrite the file
    for module, path in sorted_modules_with_paths:
        f.write(f"{module} - Path: {path}\n")






