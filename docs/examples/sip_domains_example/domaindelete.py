from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.http_method import HttpMethod
from docs.examples.credentials import sid, authToken

url = 'http://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
sipDomainsConnector = ConnectorFactory(configuration).sipDomainsConnector

# delete domain
try:
    domain = sipDomainsConnector.deleteDomain('DomainSid')
    if domain.sid:
        print('Domain Successfully Deleted')
except ZangException as ze:
    print(ze)
