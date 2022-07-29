# Develop docs

## Setup environment

Create a local python 3 environemnt and install requirements

```
pip install -r dev-requirements.txt
# pip-compile dev-requirements.in to update or add new dev requirements
```

## Activate pre-commits

There are github actions to check code with `flake8` and `black` so
it will be usefull to activate pre-commits

```
pre-commit install
```
