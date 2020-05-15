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
  
> Download the chrome and gecko drivers & place them in `/usr/local/bin` in order to add them to the PATH variable
- Browsers (Chrome, Safari, Firefox)
- [Browser drivers](https://www.selenium.dev/downloads) (Safari doesn't need a browser driver)

## Command Line Example

`pipenv run pytest --locale=es --env=dev --browserdriver=chrome -n=4 --dist=loadscope` 

Breakdown of this command:
- `pipenv run pytest`: run `pytest` in the Python virtual environment created by
  `pipenv`
- `--locale=es`: set testing locale to Spanish; omit flag to test English
- `--env=dev`: set testing environment to development; omit flag to test
  production
- `--browserdriver=chrome`: set testing browser to chrome; `firefox` and `safari` are also available
- `-n=4`: run tests in parallel using `4` separate browser instances (required flag to separately test creating internship and applying for an internship)
- `--dist=loadscope`: designate a specific browser window for each test file
  when testing in parallel; without this flag, pytest by default consolidates
  tests from all test files into a single list, randomly chooses a test from
  that list, and sends that test to an arbitrary browser window - not the
  desired behavior as we separate tests into files to target different urls/DOMs