# BEHAVE FRAMEWORK
Test Automation Framework Using Python and Behave BDD to test REST services and API

Swagger For Demo: http://petstore.swagger.io/

## Installation
- Create virtual environment directory by command : ` python -m venv env` 
- Activate the virtual environment by command : `env/Script/activate` or  ` source env/bin/activate`
- Install library dependency by command : ` pip install -r requirements.txt`
- Install Report Portal Agent for Behave by command `pip install behave-reportportal`
+ Intall Scoop if the os is window and Brew if the os is Mac before installing the allure.

## Project Structure
- Overall structure is followed as:
```
+-- requirements.txt //store the library dependencies
+-- behave_rest/
    +-- environment.py //contain common actions related to scenarios
+-- features/
    +-- config.yaml //store project config (urls, global variables, etc.)
    +-- environment.py //context setup steps (e.g. load from config.yaml)
    +-- steps/
        +-- base_steps.py // defines common steps
        +-- init_test_conditions.py //init test data before executing the TCs
        +-- *_steps.py // steps related to corresponding feature 
    +-- testcase/
        +-- *.feature //test cases to verify the APIs
    
+-- resources/
    -- *.json // test data

+-- reports
    +-- *.xls // test report utilized to import into Azure DevOps

 +-- utilities/
    +-- *_utilities.py //define a utility library 
```

## Run Tets
```bash

# choose testing environment (e.g., qa environment)
export env=qa

# execute all feature files without using the shell script (all tests)
behave

# execute a specific feature without using the shell script
behave features/regression_test/sample.feature

# show the printed output without using the shell script
behave --no-capture

# run features with specific tag without using the shell script
behave --tags=smoke

# run features with specific tags without using the shell script
behave --tags=us_6485,us_6486,us_6487

# skip printing the unwanted tags in the console without using the shell script
behave --no-skipped

# run features with specific tags in parallel
behavex --tags=parallel-test --no-capture --parallel-processes 2 --parallel-scheme scenario

# run features with specific tags and generate the allure report by using the shell script
sh shell_script/demo_executation.sh

```