class AuthenticationRequest(object):
    """
    Authentication Request object for COA

    Attributes:
        request_token (str): The request token used for requesting authentication from the user
        auth_url (str): The URL for the user to use for authentication
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
    Permissions that you currently have access to

    Attributes:
        view_public_information (bool): Can view public information such as a Username and Avatar
        view_email_address (bool): Can view the users Email Address
        read_personal_information (bool): Can read personal information such as First Name, Last Name and Birthday
        send_telegram_notifications (bool): Can send notifications to the users Telegram Account
        make_purchases (bool): Can request purchases from the user (Intellivoid only)
    """

    def __init__(self, dict_object):
        """
        Permissions Constructor

        :param dict dict_object:
        """

        self.view_public_information = False
        self.view_email_address = False
        self.read_personal_information = False
        self.send_telegram_notifications = False
        self.make_purchases = False

        if 'view_public_information' in dict_object['permissions']:
            self.view_public_information = dict_object['permissions']['view_public_information']

        if 'view_email_address' in dict_object['permissions']:
            self.view_email_address = dict_object['permissions']['view_email_address']

        if 'read_personal_information' in dict_object['permissions']:
            self.read_personal_information = dict_object['permissions']['read_personal_information']

        if 'send_telegram_notifications' in dict_object['permissions']:
            self.send_telegram_notifications = dict_object['permissions']['send_telegram_notifications']

        if 'make_purchases' in dict_object['permissions']:
            self.make_purchases = dict_object['permissions']['make_purchases']
