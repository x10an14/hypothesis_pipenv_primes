# Hypothesis Test-framework and Pipenv playground

## Install instructions:
1. Install [Pipenv](http://docs.pipenv.org/en/latest/advanced.html#fancy-installation-of-pipenv): 
    1. `curl https://raw.githubusercontent.com/mitsuhiko/pipsi/master/get-pipsi.py | python`
    2. `pipsi install pew`
    3. `pipsi install pipenv`
2. `cd` into repo folder.
3. `pipenv --three` or `pipenv --python <your python3 flavor>`
4. Choose between (may be mutually exclusive, depending on dependencies):
    1. `pipenv install` for using library (currently not necessary due to zero dependencies).
    2. `pipenv install --dev` for developing.

## Testing instructions:
1. Follow "Install instructions" and step 4.ii.
2. In root of repo folder; `pipenv shell`
3. `python -m pytest tests/ --hypothesis-show-statistics`

## Development instructions:
Remember to commit any changes to [Pipfile](https://github.com/x10an14/hypothesis_pipenv_primes/blob/master/Pipfile) or [Pipfile.lock](https://github.com/x10an14/hypothesis_pipenv_primes/blob/master/Pipfile.lock) to git.
### If you want to install a new library dependency:
`pipenv install <pypi package or something>`
### If you want to install a new dev-dependency:
`pipenv install --dev <pypi package or something>`
