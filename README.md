# Amazon Automation
* https://www.amazon.in/

## Scenarios Automated:
1. search for a product and add to cart


## Implementation
  * Language used: Python (3.10)
  * Frameworks used: Selenium, pytest, Cucumber
  * Page Object Method (POM), is used to implement the framework, all the
functionalities which lie inside that page becomes methods of the corresponding
class.
  * All the feature files contains in feature folder and all the tests and pages objects are resides in steps and pages
    folders respectively.
  * base_page.py contains all the reusable libraries like click, send_keys, wait etc

# Links

* [Github link to clone project](https://github.com/vishnumj005/amazon-pytest-bdd.git)
* please note: the currently used version for python is 3.10.
* Install requirements before executing the scripts
  file before running the script.

# How to run test?

1. Via Terminal

    * Run `pytest -s <test file>`
    * Run `pytest -m <tag name>`

2. Via PyCharm
    * Run directly from the test file


# Folder Structure

	.
	├── Root
	│     ├── steps                              # Test File
	│     │     └── test_add_to_cart_steps.py
	│     ├── feature
	│     │     └── add_to_cart.feature          # Test scenarios
	│     ├── config                             # Configurations
	│     │     ├── driver
	│     │     │     └──driverfactory.py
	│     │     └── base_config.py
	│     ├── pages                             # Pages
	│     │     ├── base
	│     │     │     └──base_page.py
	│     │     └── add_to_cart_page.py
    │     ├── conftest.py                       # pretest and post test
    │     ├── globals.py                        # Global data
    │     ├── requriements.txt                  # Required libraries
    │     └── pytest.ini                        # configuration ini file

