from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'


configuration = Configuration(sid, authToken, url=url)
ipAclConnector = ConnectorFactory(configuration).ipAccessControlListsConnector

# update access control list ip
try:
    aclIp = ipAclConnector.updateAclIp(
        'IpAclSid', 'IpSid', 'NewFriendlyName',
        '0.0.0.0')#ACL SID, IP SID, NEW FRIENDLY NAME, NEW IP ADDRESS
    view = vars(aclIp)
    print('\n')
    for item in view:
        print (item , ' : ' , view[item])
        
except ZangException as ze:
    print(ze)
