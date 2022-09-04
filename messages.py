class Message:
    def __init__(self):
        self.MESSAGES_DICTIONARY = {}
        self.success_code = 100000
        self.warning_code = 200000
        self.error_code = 300000

    def success(self, message):
        self.success_code += 1
        ret = {'status': 'success', 'code': self.success_code, 'message': message}
        self.MESSAGES_DICTIONARY[self.success_code] = ret
        return ret

    def warning(self, message):
        self.warning_code += 1
        ret = {'status': 'warning', 'code': self.warning_code, 'message': message}
        self.MESSAGES_DICTIONARY[self.warning_code] = ret
        return ret

    def error(self, message):
        self.error_code += 1
        ret = {'status': 'error', 'code': self.error_code, 'message': message}
        self.MESSAGES_DICTIONARY[self.error_code] = ret
        return ret


msg = Message()

# successes
YOUR_REGISTRATION_WAS_SUCCESSFUL = msg.success('Your registration was successful.')
PLEASE_TRY_WITH_ANOTHER_USERNAME_OR_EMAIL = msg.warning('Please try with another username or email.')
PASSWORD_PATTERN = msg.warning("The password pattern is as follows:\n"
                               "- The number of characters in the password must be more than or equal to eight "
                               "characters and less than thirty one characters\n"
                               "- The password must be a combination of numbers, lowercase English letters, uppercase "
                               "English letters.")
BEANSERNAME_PATTERN = msg.warning("The beansername pattern is as follows:\n"
                                  "- The number of characters in the beansername must be more than or equal to three "
                                  "characters and less than fifteen characters\n"
                                  "- The beansername must be a combination of numbers, lowercase English letters, "
                                  "uppercase English letters.")
YOUR_PASSWORD_IS_NOT_ACCEPTABLE = msg.error('Your password is not acceptable.')
THE_BEANSER_WITH_THIS_PROFILE_IS_ALREADY_REGISTERED = msg.error('The beanser with this profile is already registered.')
PLEASE_CONFIRM_YOUR_EMAIL_AS_SOON_AS_POSSIBLE = msg.warning('Please confirm your email as soon as possible.')
AN_UNKNOWN_ERROR_HAS_OCCURRED = msg.error('An unknown error has occurred.')
PLEASE_CONTACT_SUPPORT = msg.warning('Please contact support.')
ACCESS_TO_THIS_AREA_IS_PROHIBITED = msg.error('Access to this area is prohibited.')
PLEASE_DO_NOT_TRY_AGAIN = msg.warning('Please do not try again.')
THERE_IS_NO_DATA_WITH_THIS_ID = msg.error('There is no data with this ID.')

# messages dictionary
MESSAGES_DICTIONARY = msg.MESSAGES_DICTIONARY
