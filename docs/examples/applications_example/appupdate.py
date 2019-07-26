from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.domain.enums.http_method import HttpMethod

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
applicationsConnector = ConnectorFactory(configuration).applicationsConnector


# update application
try:
    application = applicationsConnector.updateApplication(
        applicationSid='PlaceApplicationSID',
        friendlyName='updatedtest2',
        voiceUrl='voiceUrl',
        voiceMethod=HttpMethod.POST,
        voiceFallbackUrl='fallbackUrl',
        voiceFallbackMethod=HttpMethod.GET,
        voiceCallerIdLookup=True,
        smsUrl='smsUrl',
        smsMethod=HttpMethod.POST,
        smsFallbackUrl='smsFallbackUrl',
        smsFallbackMethod=HttpMethod.GET,
        heartbeatUrl='heartbeatUrl',
        heartbeatMethod=HttpMethod.GET,
        statusCallback='statusCallback',
        statusCallbackMethod=HttpMethod.POST,
        hangupCallback='hangupCallback',
        hangupCallbackMethod=HttpMethod.GET)
    view = vars(application)
    print('\n')
    for item in view:
        print (item , ' : ' , view[item])
except ZangException as ze:
    print(ze)
