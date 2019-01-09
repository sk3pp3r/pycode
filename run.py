#!/usr/bin/python3

import git
import os
import shutil

git_url = "https://github.com/sk3pp3r/tp25.git" # url of repo
repo_dir = "/home/haimc/btr" # location to clone
branch = "master" 

if os.path.exists(repo_dir):
    shutil.rmtree(repo_dir)

r = git.Repo.clone_from(git_url, repo_dir, branch=branch, recursive=True)

