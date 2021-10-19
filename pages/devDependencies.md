# Development dependencies

This site's development dependencies are as follows:

```sh
brew install pandoc python yarn
```

## Python virtual environment

```sh
python3 -m venv virtual
. ./virtual/bin/activate
pip install -U pip wheel
pip install -r requirements.txt
pip install -e .
```

## Node modules

```sh
yarn
```
