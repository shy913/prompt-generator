import os
import subprocess
import sys
import re

def check_git_installed():
    """Check if git is installed on the system."""
    try:
        subprocess.run(["git", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        return False

def is_git_repository():
    """Check if the current directory is a git repository."""
    return os.path.isdir(".git")

def initialize_repository():
    """Initialize a new git repository if one doesn't exist."""
    if not is_git_repository():
        print("Initializing git repository...")
        subprocess.run(["git", "init"], check=True)
        return True
    return False

def get_remote_url():
    """Get the current remote URL if it exists."""
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()
    except subprocess.SubprocessError:
        return None

def add_remote(url):
    """Add a remote repository URL."""
    current_url = get_remote_url()
    
    if current_url is None:
        print(f"Adding remote: {url}")
        subprocess.run(["git", "remote", "add", "origin", url], check=True)
    elif current_url != url:
        print(f"Updating remote from {current_url} to {url}")
        subprocess.run(["git", "remote", "set-url", "origin", url], check=True)
    else:
        print(f"Remote already set to {url}")

def add_files():
    """Add all files to git."""
    print("Adding files to git...")
    subprocess.run(["git", "add", "."], check=True)

def commit_changes(message):
    """Commit changes with the given message."""
    print(f"Committing changes: {message}")
    subprocess.run(["git", "commit", "-m", message], check=True)

def push_to_remote(branch="main"):
    """Push changes to the remote repository."""
    print(f"Pushing to remote branch: {branch}")
    try:
        subprocess.run(["git", "push", "-u", "origin", branch], check=True)
    except subprocess.CalledProcessError:
        # If the branch doesn't exist on remote, create it
        print(f"Branch {branch} doesn't exist on remote. Creating it...")
        subprocess.run(["git", "push", "--set-upstream", "origin", branch], check=True)

def validate_github_url(url):
    """Validate if the provided URL is a valid GitHub repository URL."""
    pattern = r'^(https://github\.com/|git@github\.com:)[\w.-]+/[\w.-]+(.git)?$'
    return re.match(pattern, url) is not None

def main():
    """Main function to push the project to GitHub."""
    print("=== Push to GitHub ===")
    
    # Check if git is installed
    if not check_git_installed():
        print("Error: Git is not installed or not in the PATH.")
        print("Please install Git from https://git-scm.com/downloads")
        sys.exit(1)
    
    # Initialize repository if needed
    initialize_repository()
    
    # Get GitHub repository URL
    github_url = input("Enter GitHub repository URL (e.g., https://github.com/username/repo.git): ").strip()
    
    # Validate GitHub URL
    if not validate_github_url(github_url):
        print("Error: Invalid GitHub repository URL.")
        print("URL should be in the format: https://github.com/username/repo.git or git@github.com:username/repo.git")
        sys.exit(1)
    
    # Add remote
    add_remote(github_url)
    
    # Add all files
    add_files()
    
    # Get commit message
    commit_message = input("Enter commit message: ").strip()
    if not commit_message:
        commit_message = "Update repository"
    
    # Commit changes
    commit_changes(commit_message)
    
    # Get branch name
    branch = input("Enter branch name (default: main): ").strip()
    if not branch:
        branch = "main"
    
    # Push to remote
    push_to_remote(branch)
    
    print("Successfully pushed to GitHub!")

if __name__ == "__main__":
    main()