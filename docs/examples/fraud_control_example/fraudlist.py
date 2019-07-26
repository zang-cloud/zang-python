from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory


from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
fraudControlConnector = ConnectorFactory(configuration).fraudControlConnector


# list fraud control resources
try:
    result = fraudControlConnector.listFraudControlResources(0, 33)
    view = vars(result)
    print('\n')
    for item in view:
        print (item , ' : ' , view[item])
    if result and result.elements:
        for result in result.elements:
            view = vars(result)
            print('\n')
            for item in view:
                    print (item , ' : ' , view[item])
except ZangException as ze:
    print(ze)
