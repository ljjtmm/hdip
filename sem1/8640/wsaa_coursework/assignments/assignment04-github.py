
import os
from git import Repo
from github import Github

def replace_text(file_path, old, new):
    # Read in the file
    with open(file_path, 'r') as file:
        data = file.read()

    # Carry out our replacement
    data = data.replace(old, new)

    # Write this to the same file
    with open(file_path, 'w') as file:
        file.write(data)

def commit_changes(repo, file_path, commit_msg):
    # Add the modified file to the staging area
    repo.index.add([file_path])

    # Commit changes
    repo.index.commit(commit_msg)

    # Push changes to the remote repository
    origin = repo.remote(name="origin")
    origin.push()

def main():
    # Retrieve the access token from our environment variable and initialise with our token
    access_token = os.environ.get("GITHUB_ACCESS_TOKEN")
    g = Github(access_token)

    # Define the user, repository, and directory within our repository
    user = g.get_user("ljjtmm")
    repo = user.get_repo("hdip")

    # Define the local repository path
    repo_path = os.path.dirname(os.path.abspath(__file__))
    repo_obj = Repo(repo_path)

    # # Define the directory and file name within the repository
    file_name = "assignment04-data.csv"
    file_path = os.path.join(repo_path, file_name)

    # Replace text in the local file
    old = "Andrew"
    new = "Lee"
    replace_text(file_path, old, new)

    # Commit and push changes
    commit_message = f"Replaced instances of '{old}' with '{new}'"
    commit_changes(repo_obj, file_path, commit_message)

    print("Changes committed and pushed successfully to the repository.")

if __name__ == '__main__':
    main()
