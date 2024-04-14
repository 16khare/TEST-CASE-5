import json
import subprocess

def build_module(module):
    if ":" in module:
        group_id, artifact_id, version = module.split(":")
        command = f"mvn clean install -DgroupId={group_id} -DartifactId={artifact_id} -Dversion={version}"
    else:
        command = f"mvn clean install -DartifactId={module}"

    module_dir = os.path.join(os.getcwd(), artifact_id)

    if os.path.exists(module_dir):
        print(f"Module {artifact_id} has already been built.")
        return

    
    # Capture the output of the build command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"Module {module} built successfully.")
        print(result.stdout)  # Print the build output
    else:
        print(f"Error building module {module}.")
        print(result.stderr)  # Print any error output

with open("sorted_modules.txt") as f:
    for line in f:
        module = line.strip()
        if module:
            print(f"Building module: {module}")
            build_module(module)