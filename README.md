# Hypothesis Test-framework and Pipenv playground

## Install instructions:
1. Install [Pipenv](http://docs.pipenv.org/en/latest/advanced.html#fancy-installation-of-pipenv): `curl https://raw.githubusercontent.com/mitsuhiko/pipsi/master/get-pipsi.py | python`
2. `cd` into repo folder.
3. `pipenv --three` or `pipenv --python <your python3 flavor>`
4. Choose between (may be mutually exclusive, depending on dependencies):
    1. `pipenv install` for using library (currently not necessary due to zero dependencies).
    2. `pipenv install --dev` for developing.

## Testing instructions:
1. Follow "Install instructions" and step 4.ii.
2. In root of repo folder; `pipenv shell`
3. `python -m pytest tests/ --hypothesis-show-statistics`
