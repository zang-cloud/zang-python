from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'


configuration = Configuration(sid, authToken, url=url)
ipAclConnector = ConnectorFactory(configuration).ipAccessControlListsConnector

# add access control list ip
try:
    aclIp = ipAclConnector.addAclIp(
        'IpAclSid', 'IpFriendlyName', 'PublicIpAddress')
    view = vars(aclIp)
    print('\n')
    for item in view:
        print (item , ' : ' , view[item])
        
except ZangException as ze:
    print(ze)
