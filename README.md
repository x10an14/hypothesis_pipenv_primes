# Hypothesis Test-framework and Pipenv playground

## Install instructions:
1. Install [Pipenv](curl https://raw.githubusercontent.com/mitsuhiko/pipsi/master/get-pipsi.py | python)<sup>1</sup>
2. `cd` into repo folder.
3. `pipenv --three` or `pipenv --python <your python3 flavor>`
4. Choose between (may be mutually exclusive, depending on dependencies):
    1. `pipenv install -r Pipfile.lock` for using library.
    2. `pipenv install -r --dev Pipfile` for developing.

## Testing instructions:
1. Follow "Install instructions" and step 4.2.
2. In root of repo folder; `pipenv shell`
3. `python -m pytest tests/ --hypothesis-show-statistics`
