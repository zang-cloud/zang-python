from datetime import date
from zang.exceptions.zang_exception import ZangException

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.domain.enums.conference_status import ConferenceStatus

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
conferencesConnector = ConnectorFactory(configuration).conferencesConnector

# view participants
try:
    participants = conferencesConnector.listParticipants(
        'ConferenceSid', False, False, 0, 33)
    view = vars(participants)
    print('\n')
    for item in view:
        print (item , ' : ' , view[item])
except ZangException as ze:
    print(ze)
