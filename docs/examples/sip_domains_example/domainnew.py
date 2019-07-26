from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.http_method import HttpMethod
from docs.examples.credentials import sid, authToken

url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
sipDomainsConnector = ConnectorFactory(configuration).sipDomainsConnector

# create domain
try:
    domain = sipDomainsConnector.createDomain(
        domainName='DomainName',            #Tosses 400 Error when domainName not unique
        friendlyName='DomainFriendlyName',
        voiceUrl='',
        voiceMethod=HttpMethod.POST,
        voiceFallbackUrl='',
        voiceFallbackMethod=HttpMethod.GET)
    print(domain.sid)
except ZangException as ze:
    print(ze)
