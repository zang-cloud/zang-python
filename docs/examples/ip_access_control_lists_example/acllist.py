from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'


configuration = Configuration(sid, authToken, url=url)
ipAclConnector = ConnectorFactory(configuration).ipAccessControlListsConnector

# list ip access control lists
try:
    ipAcls = ipAclConnector.listIpAcls(0, 33)
    view = vars(ipAcls)
    print('\n')
    for item in view:
        print (item , ' : ' , view[item])
    for acls in ipAcls.elements:
        view = vars(acls)
        print('\n')
        for item in view:
            print (item , ' : ' , view[item])
        
except ZangException as ze:
    print(ze)
