import os
import requests
from dotenv import load_dotenv

load_dotenv()


class DataverseWebAPIAuthHandler(object):
    LOGIN_URL = 'https://login.microsoftonline.com/{0}/oauth2/token'
    TENANT_ID = os.environ.get('TENANT_ID')
    APP_ID = os.environ.get('APP_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    GRANT_TYPE = 'client_credentials'
    DYNAMICS_ENV = os.environ.get('DYNAMICS_ENV')
    WEB_API_VERSION = os.environ.get('WEB_API_VERSION')
    RESOURCE = 'https://{}.crm7.dynamics.com/'.format(DYNAMICS_ENV)
    DATAVERSE_DATA_URL = '{0}api/data/v{1}/'.format(RESOURCE, WEB_API_VERSION)
    response = None

    def __init__(self):
        self.init()

    def init(self):
        self.response = requests.post(self.LOGIN_URL.format(self.TENANT_ID), data={
            'tenant_id': self.TENANT_ID,
            'client_id': self.APP_ID,
            'client_secret': self.CLIENT_SECRET,
            'grant_type': self.GRANT_TYPE,
            'resource': self.RESOURCE
        })

    def get_auth_params(self):
        access_token = self.response.json().get('access_token')
        token_type = self.response.json().get('token_type')
        return (access_token, token_type)
