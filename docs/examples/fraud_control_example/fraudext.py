from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory


from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
fraudControlConnector = ConnectorFactory(configuration).fraudControlConnector

# extend destination: extends a destinations authorization expiration by 30 days
try:
    rule = fraudControlConnector.extendDestinationAuthorization('HR')
    print("extended for another 30days!")
except ZangException as ze:
    print(ze)
