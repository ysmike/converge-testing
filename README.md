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
  
> Make sure to download the drivers for the correct OS & browser version. Place
the browsers in root directory.
- Browsers (Chrome, MS Edge, Firefox, etc.)
- [Browser drivers](https://www.selenium.dev/downloads)

## Command Line Example

`pipenv run pytest --locale es --env dev -n=4 --dist=loadscope` 

Breakdown of this command:
- `pipenv run pytest`: run `pytest` in the Python virtual environment created by
  `pipenv`
- `--locale es`: set locale to Spanish; omit flag to test English
- `--env dev`: set testing environment to development; omit flag to test
  production
- `-n=4 --dist=loadscope`: run tests in parallel using `4` separate browser
  instances; use a single browser for each test file (vs. picking random tests
  out of any test files)