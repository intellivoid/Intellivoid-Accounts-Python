import six


class AuthenticationError(Exception):
    """COA Authentication exception"""

    def __init__(self, reason, response=None, error_code=None):
        self.reason = six.text_type(reason)
        self.response = response
        self.error_code = error_code
        super(AuthenticationError, self).__init__(reason)

    def __str__(self):
        return self.reason
