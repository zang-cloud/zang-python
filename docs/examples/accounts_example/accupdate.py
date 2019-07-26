from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.exceptions.zang_exception import ZangException

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url)
accountsConnector = ConnectorFactory(configuration).accountsConnector

try:
    newfriendlyName='writefriendlynamehere'
    account = accountsConnector.viewAccount()
    accountsConnector.updateAccount(newfriendlyName)
    print("Friendly name was:",account.friendlyName,"and is now set to:",newfriendlyName)
except ZangException as e:
    print(e)
