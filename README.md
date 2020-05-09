# YWAM Converge Web UI Test Suite
Web browser testing for [YWAM Converge](https://ywamconverge.org/) via Selenium
& pytest

## Prerequisites: 
- [python3](https://www.python.org/download/releases/3.0/)
- [pipenv](https://pipenv-fork.readthedocs.io/en/latest/)

> Run 'pipenv install' to install below packages in a virtual environment
- selenium
- pytest
- pytest-xdist
- pyyaml
- requests
  
> Download the applicable browser drivers & place them in root directory
- Browsers (Chrome, MS Edge, Firefox, etc.)
- [Browser drivers](https://www.selenium.dev/downloads)

## Command Line Example

`pipenv run pytest --locale=es --env=dev -n=4 --dist=loadscope` 

Breakdown of this command:
- `pipenv run pytest`: run `pytest` in the Python virtual environment created by
  `pipenv`
- `--locale=es`: set testing locale to Spanish; omit flag to test English
- `--env=dev`: set testing environment to development; omit flag to test
  production
- `-n=4`: run tests in parallel using `4` separate browser instances
- `--dist=loadscope`: designate a specific browser window for each test file
  when testing in parallel; without this flag, pytest by default consolidates
  tests from all test files into a single list, randomly chooses a test from
  that list, and sends that test to an arbitrary browser window - not the
  desired behavior as we separate tests into files to target different urls/DOMs