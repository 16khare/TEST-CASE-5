import git
from collections import defaultdict
from toposort import toposort

# Read text file and parse module dependencies
modules = defaultdict(list)
with open('modules.txt', 'r') as file:
    for line in file:
        parts = line.strip().split(':')
        module = parts[1]
        dependencies = parts[2].split(',') if parts[2] != 'None' else []
        modules[module] = dependencies

# Build dependency graph
graph = {module: set(dependencies) for module, dependencies in modules.items()}

# Perform topological sort
build_order = list(toposort(graph))

# Visit Git repository folders and build modules
repo = git.Repo('/path/to/your/git/repo')
for module in build_order:
    if module in repo.tree():
        # Build module
        print(f'Building {module}...')