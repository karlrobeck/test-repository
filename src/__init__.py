import os
from typer import Typer

app = Typer()


@app.command("init")
def git_init():
    """
    git init
    git commit -m "first commit"
    git branch -M "branch"
    git remote add origin "link"
    git push -u origin "branch"
    """

    branch_name: str = input("branch name:")
    commit_message: str = input("commit message: ")
    repositoyry_link: str = input("github link: ")
    add_files = (
        True
        if input("would you like to add current file system? ").lower() in "yes"
        else False
    )

    os.system("git init")
    if add_files:
        os.system("git add .")
    os.system(f'git commit -m "{commit_message}"')
    os.system(f"git branch -M {branch_name}")
    os.system(f'git remote add origin "{repositoyry_link}"')
    os.system(f"git push -u -f origin {branch_name}")


@app.command("add")
def git_add():
    pass


@app.command("rm")
def git_rm():
    pass


@app.command("commit")
def git_commit(message: str):
    pass


@app.command("push")
def git_push(*args: str):
    pass


@app.command("pull")
def git_pull():
    pass


@app.command("fetch")
def git_fetch():
    pass


@app.command("branch")
def git_branch():
    pass


@app.command("checkout")
def git_checkout():
    pass


@app.command("reset")
def git_reset():
    pass


if __name__ == "__main__":
    app()
