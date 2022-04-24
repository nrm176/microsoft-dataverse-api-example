import requests
from dataversewebapiauthhandler import DataverseWebAPIAuthHandler

if __name__ == '__main__':
    auth_handler = DataverseWebAPIAuthHandler()
    access_token, token_type = auth_handler.get_auth_params()

    ACCOUNTS_DATA_URL = f'{auth_handler.DATAVERSE_DATA_URL}accounts'
    accounts = requests.get(ACCOUNTS_DATA_URL, headers={'Authorization': f'{token_type} {access_token}'})
    print(accounts.json())
