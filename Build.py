import json
import subprocess

def build_module(module):
    if ":" in module:
        group_id, artifact_id, version = module.split(":")
        command = f"mvn clean install -DgroupId={group_id} -DartifactId={artifact_id} -Dversion={version}"
    else:
        command = f"mvn clean install -DartifactId={module}"
    subprocess.run(command, shell=True)

def get_module_paths(module_name):
    with open("build.dag") as f:
        data = json.load(f)
    if "nodes" in data:
        for node in data["nodes"]:
            if node["name"] == module_name:
                return node["path"]
    return None

with open("sorted_modules.txt") as f:
    for line in f:
        module = line.strip()
        if module:
            print(f"Building module: {module}")
            build_module(module)
            path = get_module_paths(module.split(":")[-1])
            if path:
                print(f"Module path: {path}")