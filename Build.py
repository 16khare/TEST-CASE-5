import git
import os
import subprocess

# Read module names from sorted_modules.txt
with open('sorted_modules.txt', 'r') as file:
    module_names = [line.strip() for line in file]

# Clone the repository
repo_url = 'git@github.com:16khare/TEST-CASE-5.git'
repo_dir = 'your_repo'
git.Repo.clone_from(repo_url, repo_dir)

# Navigate to each module's directory and build it
repo = git.Repo(repo_dir)
for module_name in module_names:
    module_path = os.path.join(repo_dir, module_name)

    # Check if the module directory exists
    if os.path.isdir(module_path):
        os.chdir(module_path)

        # Run Maven build command
        build_command = 'mvn clean install'
        subprocess.run(build_command, shell=True)

        # Go back to the root directory
        os.chdir(repo_dir)
    else:
        print(f'Module {module_name} not found in the repository')