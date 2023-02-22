from base_steps import *



@step('Creating user request is sent')
def create_user_request(context) -> None:
    """
    Create new user with info as username, password, email, phoner, userStatus, lastName, firstName
    """
    