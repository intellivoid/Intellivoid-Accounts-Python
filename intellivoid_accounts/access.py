import six
import json
import requests

from intellivoid_accounts.auth import COA
from intellivoid_accounts.objects import Permissions
from intellivoid_accounts.exception import AuthenticationError


class Access(object):

    def __init__(self, coa_authentication, access_token):
        """
        Public Constructor

        :param COA coa_authentication:
        :param str access_token:
        """
        self.coa_authentication = coa_authentication
        if type(access_token) == six.text_type:
            access_token = access_token.encode('ascii')
        self.access_token = access_token

    def get_permissions(self):
        """
        Gets the current permissions that you currently have access to
        :return:
        """
        parameters = {
            "action": "check_permissions",
            "access_token": self.access_token
        }
        self.coa_authentication.apply_authentication(parameters)

        try:
            r = requests.post(self.coa_authentication.get_coa_url(), parameters)
            print(r.text)
            response = json.loads(r.text)
        except Exception as e:
            raise AuthenticationError(e)

        if not response["status"]:
            raise AuthenticationError(response["message"], r.text, response["error_code"])
        return Permissions(response)