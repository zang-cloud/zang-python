from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.exceptions.zang_exception import ZangException

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url)
accountsConnector = ConnectorFactory(configuration).accountsConnector

try:
    account = accountsConnector.viewAccount()
    print("Friendly Name",account.friendlyName,"\n", "Account Balance", account.accountBalance,"\n","Sid", account.sid,"\n","Status",account.status,"\n","Time Zone",account.timeZone,"\n","Date Created", account.dateCreated,"\n","Date Updated", account.dateUpdated)#available inputs are: ['friendlyName','accountBalance','sid','status'
    print("URI for calls is:",account.subresourceUris.incomingPhoneNumbers)#available uris are: ['availablePhoneNumbers', 'bna', 'calls', 'carrier', 'cnam', 'conferences', 'fraud', 'incomingPhoneNumbers', 'notifications', 'transactions', 'transcriptions', 'usages']
except ZangException as e:
    print(e)
