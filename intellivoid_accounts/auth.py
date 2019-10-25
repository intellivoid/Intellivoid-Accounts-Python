import six
import json
import time
import requests

from intellivoid_accounts.exception import AuthenticationError
from intellivoid_accounts.objects import AuthenticationRequest


class COA(object):
    """
    COA Authentication Object which contains
    """

    COA_HOST = 'accounts.intellivoid.info'
    COA_ROOT = '/auth/coa'
    COA_SECURED = True

    def __init__(self, application_id, secret_key):
        """
        COA Constructor
        :param str application_id:
        :param str secret_key:
        """
        if type(application_id) == six.text_type:
            application_id = application_id.encode('ascii')

        if type(secret_key) == six.text_type:
            secret_key = secret_key.encode('ascii')

        self.application_id = application_id
        self.secret_key = secret_key

    def apply_application(self, parameters):
        """
        Applies Application ID to parameters (dict)
        :param dict parameters:
        :return:
        """

        return parameters.update({
            "application_id": self.application_id
        })

    def apply_authentication(self, parameters):
        """
        Applies Application ID and Secret Key to parameters (dict)
        :param dict parameters:
        :return:
        """

        return parameters.update({
            "application_id": self.application_id,
            "secret_key": self.secret_key
        })

    def get_coa_url(self):

        protocol = "http"
        if self.COA_SECURED:
            protocol = "https"
        return "{0}://{1}{2}".format(protocol, self.COA_HOST, self.COA_ROOT)

    def get_authentication_request(self, redirect=None):
        parameters = {"action": "create_authentication_request"}
        self.apply_application(parameters)
        if redirect is not None:
            parameters.update({"redirect": redirect})

        try:
            r = requests.post(self.get_coa_url(), parameters)
            response = json.loads(r.text)
        except Exception as e:
            raise AuthenticationError(e)

        if not response["status"]:
            raise AuthenticationError(response["message"], r.text, response["error_code"])
        return AuthenticationRequest(response)

    def get_access_token(self, request_token):
        parameters = {"action": "get_access_code", "request_token": request_token}
        self.apply_application(parameters)

        try:
            r = requests.post(self.get_coa_url(), parameters)
            response = json.loads(r.text)
        except Exception as e:
            raise AuthenticationError(e)

        if not response["status"]:
            raise AuthenticationError(response["message"], r.text, response["error_code"])
        return response["access_token"]

    def poll_access_token(self, request_token, timeout=0):
        current_counter = 0

        while True:
            if timeout != 0:
                if current_counter == timeout:
                    raise TimeoutError()
            try:
                access_token = self.get_access_token(request_token)
                return access_token
            except AuthenticationError as ae:
                if ae.error_code != 41:
                    raise ae
                time.sleep(1)
                current_counter += 1
