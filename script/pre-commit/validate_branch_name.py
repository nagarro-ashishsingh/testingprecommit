import sys
import re
import subprocess


def is_valid_branch_name(branch_name):
    valid_patterns = [
        re.compile(r"^main$"),
        re.compile(r"^release$"),
        re.compile(r"^(feature|fix|hotfix)\/SK-\d*-[a-zA-Z0-9_-]+$"),
    ]

    return any(pattern.match(branch_name) for pattern in valid_patterns)


def get_current_branch():
    try:
        # Run the "git branch --show-current" command to get the current branch
        result = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True, check=True)
        # Extract and return the branch name
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        # Handle errors, for example, when not in a Git repository
        return None


# Example usage
print(sys.argv)
branch_name = get_current_branch()
# branch_name = sys.argv[1]
if branch_name is not None:
    print(f"The current branch is: {branch_name}")
else:
    print("Not in a Git repository or unable to determine the current branch.")

if not is_valid_branch_name(branch_name):
    print("Invalid branch name:", branch_name)
    print(
        "Branch names must start with 'main', 'feature', 'fix', or 'hotfix' and may also contain the Jira issue "
        "number"
    )
    sys.exit(1)
else:
    print("Branch name is fine")
