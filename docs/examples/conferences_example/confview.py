from datetime import date
from zang.exceptions.zang_exception import ZangException

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.domain.enums.conference_status import ConferenceStatus

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
conferencesConnector = ConnectorFactory(configuration).conferencesConnector


# view conference
try:
    conference = conferencesConnector.viewConference('ConferenceSid')
    print(conference.friendlyName)
except ZangException as ze:
    print(ze)
