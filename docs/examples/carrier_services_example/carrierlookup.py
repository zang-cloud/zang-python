from zang.exceptions.zang_exception import ZangException

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
carrierServicesConnector = ConnectorFactory(
    configuration).carrierServicesConnector


# carrier lookup
try:
    data = carrierServicesConnector.viewCarrierLookup('e164')   #Just calls function
    data = carrierServicesConnector.listCarrierLookups(0, 1)            #Basically listing, but only one
    for lookups in data.elements:
        view = vars(lookups)
        print('\n')
        for item in view:
            print (item , ' : ' , view[item])
except ZangException as ze:
    print(ze)
