import os
from git import Repo

def clone_repository(repo_url):
    current_dir = os.getcwd()
    target_dir = os.path.join(current_dir, repo_url.split('/')[-1].replace('.git', ''))

    try:
        print(f"Cloning from {repo_url} into {target_dir}")
        Repo.clone_from(repo_url, target_dir)
        print("Repository cloned successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
repository_url = "https://github.com/kreemkhaled112/ahmed"
clone_repository(repository_url)
