# YWAM Converge Web UI Test Suite
Web browser testing for [YWAM Converge](https://ywamconverge.org/) via Selenium
& pytest

## Prerequisites: 
- python3

> 'pipenv install' to install below packages in a virtual environment
- selenium
- pytest
- pytest-xdist
- requests
  
> Make sure to download the drivers for the correct OS & browser version. Place
the browsers in root directory.
- Browsers (Chrome, MS Edge, Firefox, etc.)
- [Browser drivers](https://www.selenium.dev/downloads)

## Notes
The emails to be used in testing which can be found in the csv files (tests/forms/*.csv) should have the string
"email" within them before the domain. This is to randomize email addresses via uuid since the test stops itself if it runs into a duplicate email.

## Command Line Example
To run a tests in parallel (via `pytest-xdist` library) with 4 browser instances
in production environment, run `pytest tests --env prod -n=4 --dist=loadscope`.
Here, `--dist=loadscope` flag is necessary to avoid errors as `pytest-dist` by
default does not run tests by groups or files. By adding the `--dist=loadscope`
flag, we make sure that a browser instance does not randomly run tests in
another file or class.
