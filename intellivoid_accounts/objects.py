class AuthenticationRequest(object):

    def __init__(self, dict_object):
        self.request_token = dict_object["request_token"]
        self.auth_url = dict_object["auth_url"]
