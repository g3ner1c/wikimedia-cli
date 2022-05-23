# Installation Guide

## Manual Installation

### bash

```bash
git clone https://github.com/g3ner1c/wikimedia-cli.git
cd wikimedia-cli
echo "alias wiki='python $(pwd)/main.py'" >> ~/.bashrc
source ~/.bashrc
```

### zsh

```zsh
git clone https://github.com/g3ner1c/wikimedia-cli.git
cd wikimedia-cli
echo "alias wiki='python $(pwd)/main.py'" >> ~/.zshrc
source ~/.zshrc
```

### fish

```fish
git clone https://github.com/g3ner1c/wikimedia-cli.git
cd wikimedia-cli
function wiki
	python (pwd)/main.py $argv
end

funcsave confgit
```
