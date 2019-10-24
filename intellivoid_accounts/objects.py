class AuthenticationRequest(object):
    """
    Authentication Request object for COA
    """
    def __init__(self, dict_object):
        """
        AuthenticationRequest Constructor
        :param dict dict_object:
        """
        self.request_token = dict_object["request_token"]
        self.auth_url = dict_object["auth_url"]


class Permissions(object):
    """
    Permissions object that represents the current permissions you have access to
    """
    def __init__(self, dict_object):
        """
        Permissions Constructor

        :param dict dict_object:
        """
        if 'view_public_information' in dict_object:
            self.view_public_information = dict_object['view_public_information']

        if 'view_email_address' in dict_object:
            self.view_email_address = dict_object['view_email_address']

        if 'read_personal_information' in dict_object:
            self.read_personal_information = dict_object['read_personal_information']

        if 'send_telegram_notifications' in dict_object:
            self.send_telegram_notifications = dict_object['send_telegram_notifications']

        if 'make_purchases' in dict_object:
            self.make_purchases = dict_object['make_purchases']