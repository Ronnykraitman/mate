#!/bin/bash

set -e
set -o pipefail
packages=("cmatrix" "asciiquarium" "samtay/tui/tetris" "nsnake" "spaceinvaders-go" "greed" "cataclysm")

brew_install() {
  for package in "${packages[@]}"; do
    brew install "$package"
  done
}


python3 -m pip install -r requirements.txt
brew_install


