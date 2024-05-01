from git import Repo

def git_pull_verbose(repo_path):
    try:
        repo = Repo(repo_path)
        origin = repo.remotes.origin
        result = origin.pull()
        for info in result:
            if info.flags > info.ERROR:
                print("Error occurred while pulling")
            else:
                print(f"Updated {info.ref}. Old commit: {info.old_commit} New commit: {info.commit}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
local_repo_path = "P:\\API\\ahmed"  # Change this to your repository's local path
git_pull_verbose(local_repo_path)
