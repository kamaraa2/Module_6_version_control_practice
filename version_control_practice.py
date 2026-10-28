"""Module 6: Individual Git and GitHub Practice.

Run this starter program, complete the TODO tasks, and commit your changes.
No outside packages are required.
"""


def show_project_info():
    """Display basic information about this version-control exercise."""
    project_name = "My GitHub Project for CST 205"
    version = "7"
    print(f"Project: {project_name}")
    print(f"Version: {version}")
    print("Git helps track changes in a software project.")


def show_git_workflow():
    """Print the basic sequence used in this exercise."""
    steps = [
        "1. Edit and save your Python file.",
        "2. Stage your changes with git add.",
        "3. Record a local commit with git commit.",
        "4. Upload your commit to GitHub with git push.",
    ]
    for step in steps:
        print(step)


def main():
    show_project_info()
    print()
    show_git_workflow()
    print()
    print("It's useful to save code changes with Git for proper record tracking and ability to revert to a previous working version")
    print("The key difference between git commit and git push is git commit after git add stages the saved changes being pushed git commit takes a snapshot on your device and git push pushes the code or that snapshot to github")

if __name__ == "__main__":
    main()
