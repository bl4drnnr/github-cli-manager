#!/usr/bin/env bash

repository="https://github.com/bl4drnnr/github-cli-manager.git"

echo "GitHub-Manager installation..."

cd "$HOME"
mkdir -p "$HOME/.ghmn"
cd "$HOME/.ghmn"

git clone "$repository"

cd "$HOME/github-cli-manager"

for EACH_PROFILE in ".profile" ".bashrc" ".bash_profile" ".zprofile" ".zshrc"
    do
      echo "alias ghmn='python3 ${HOME}/.ghmn/github-cli-manager/main.py'" >> "${HOME}/${EACH_PROFILE}"
    done

echo "GitHub-Manager have been successfully installed..."
