class _Message:
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


_msg = _Message()

_success = _msg.success
_warning = _msg.warning
_error = _msg.error
