# SeleniumAutomation
This is a python selenium UI automation test framewrok with unittest

# Overview
This is a UI automation test framework base on Selenium + unitest on python3.
* Selenium is an umbrella project encapsulating a variety of tools and libraries enabling web browser automation. 
* unittest is a built-in test framework for python. In this project it is used to construct the test framework and support functions such assertation, test cases/suites management and test report.

# Modules
There are 3 modules in this test framework:
## `core`: 
which contains base classes for testing:
 #### `element_base`
contains base class of web elements. Some common methods of elememts added. They are based on native selenium APIs and made more convinient to use.
 #### `test_case_base`
class `TestCaseBase` is inherited from `unittest.TestCase`. Defined method need to run before and after running cases/suite.
 #### `webdriver_base`
class `TestWebDriver` contains method to start webdriver for test and other method of webdriver.

## `page_objects`
which contains page objects files.
You can create specific page objects file for the web page. Each element on web page will be created as a class inherited from `ElementBase`. `__init__` should be defined with way to locate this element.

## `test`
which contains all the test cases/suite.

# Test case and Test suite
Test case in this project need to follow this model:
1. create a folder under `/test` contain test script and config file. e.g. `test/test_demo_script/test_demo_script.py` and `test/test_demo_script/config.yml`.
1. in file `test/test_demo_script/test_demo_script.py`:
    1. import page file for this test case
    1. creat a class inherited from class `TestCaseBase`
    1. define functons in this class as test cases, each function will be a test case
    1. If you put more than one functions in one test script, this test script will be a test suite.
1. in file `test/test_demo_script/config.yml`: put parameters you want to config in test cases

