from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'


configuration = Configuration(sid, authToken, url=url)
ipAclConnector = ConnectorFactory(configuration).ipAccessControlListsConnector

# delete access control list ip
try:
    aclIp = ipAclConnector.deleteAclIp(
        'IpAclSid', 'IPSid')#ACL SID, IP SID
    print('Deleted!')
        
except ZangException as ze:
    print(ze)
