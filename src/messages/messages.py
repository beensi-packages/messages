from .message import _success, _warning, _error, _msg

YOUR_REGISTRATION_WAS_SUCCESSFUL = _success('Your registration was successful.')
PLEASE_TRY_WITH_ANOTHER_USERNAME_OR_EMAIL = _warning('Please try with another username or email.')
PASSWORD_PATTERN = _warning("The password pattern is as follows:\n"
                            "- The number of characters in the password must be more than or equal to eight "
                            "characters and less than thirty one characters\n"
                            "- The password must be a combination of numbers, lowercase English letters, uppercase "
                            "English letters.")
BEANSERNAME_PATTERN = _warning("The beansername pattern is as follows:\n"
                               "- The number of characters in the beansername must be more than or equal to three "
                               "characters and less than fifteen characters\n"
                               "- The beansername must be a combination of numbers, lowercase English letters, "
                               "uppercase English letters.")
YOUR_PASSWORD_IS_NOT_ACCEPTABLE = _error('Your password is not acceptable.')
THE_BEANSER_WITH_THIS_PROFILE_IS_ALREADY_REGISTERED = _error('The beanser with this profile is already registered.')
PLEASE_CONFIRM_YOUR_EMAIL_AS_SOON_AS_POSSIBLE = _warning('Please confirm your email as soon as possible.')
AN_UNKNOWN_ERROR_HAS_OCCURRED = _error('An unknown error has occurred.')
PLEASE_CONTACT_SUPPORT = _warning('Please contact support.')
ACCESS_TO_THIS_AREA_IS_PROHIBITED = _error('Access to this area is prohibited.')
PLEASE_DO_NOT_TRY_AGAIN = _warning('Please do not try again.')
THERE_IS_NO_DATA_WITH_THIS_ID = _error('There is no data with this ID.')
THIS_TOKEN_HAS_ALREADY_BEEN_REGISTERED = _error('This token has already been registered.')
PLEASE_TRY_AGAIN = _warning('Please try again.')
AN_UNKNOWN_PROBLEM_HAS_OCCURRED = _error('An unknown problem has occurred.')
PLEASE_TRY_WITH_ANOTHER_TOKEN = _warning('Please try with another token.')
PLEASE_TRY_WITH_ANOTHER_EMAIL_ADDRESS = _warning('Please try with another email address.')

# messages dictionary
MESSAGES_DICTIONARY = _msg.MESSAGES_DICTIONARY
