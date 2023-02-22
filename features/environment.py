from yaml import safe_load
from pathlib import Path
import os


def before_all(context) -> None:
    """
    Configure before starting test execution
    """
    context.settings = safe_load(open('features/config.yaml').read())
    context.env = os.getenv('env','qa') #default env=qa if empty env parameter
    context.url = context.settings[context.env]['baseURL']
    context.petId= ""
    context.headers = {}
    context.body = {}
    context.response_code = {}
    context.response_text = {}


def before_scenario(context, scenario) -> None:
    """
    Configure before starting test scenario
    Arg:
        - scenario: scenario object
    """
    if "runner.continue_after_failed_step" in scenario.effective_tags:
        scenario.continue_after_failed_step = True
    return


def after_all(context) -> None:
    return None
