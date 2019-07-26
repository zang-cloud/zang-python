from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.http_method import HttpMethod
from docs.examples.credentials import sid, authToken

url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
sipDomainsConnector = ConnectorFactory(configuration).sipDomainsConnector

# update domain
try:
    domain = sipDomainsConnector.updateDomain(
        'DomainSid',
        friendlyName='NewDomainFriendlyName',
        voiceUrl='VoiceUrl2',
        voiceMethod=HttpMethod.POST,)
    if domain.voiceUrl:
        print('Update successful')
except ZangException as ze:
    print(ze)
