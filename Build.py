import json
import subprocess

def build_module(module):
    if ":" in module:
        group_id, artifact_id, version = module.split(":")
        command = f"mvn clean install -DgroupId={group_id} -DartifactId={artifact_id} -Dversion={version}"
    else:
        command = f"mvn clean install -DartifactId={module}"
    subprocess.run(command, shell=True)

with open("sorted_modules.txt") as f:
    for line in f:
        module = line.strip()
        if module:
            print(f"Building module: {module}")
            build_module(module)