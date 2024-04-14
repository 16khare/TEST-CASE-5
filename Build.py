import os
import subprocess

def build_module(module):
    if ":" in module:
        group_id, artifact_id, version = module.split(":")
        command = f"mvn clean install -DgroupId={group_id} -DartifactId={artifact_id} -Dversion={version}"
    else:
        command = f"mvn clean install -DartifactId={module}"

    module_dir = os.path.join(os.getcwd(), artifact_id)

    try:
        if os.path.isdir(module_dir):
            print(f"Module {artifact_id} has already been built.")
            return
    except NameError:
        print("Error: The 'os' module is not found.")
        return

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"Module {artifact_id} built successfully.")
            print(result.stdout)  # Print the build output
        else:
            print(f"Error building module {artifact_id}.")
            print(result.stderr)  # Print any error output
    except Exception as e:
        print(f"An error occurred while building module {artifact_id}: {e}")