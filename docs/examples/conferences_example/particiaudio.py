from datetime import date
from zang.exceptions.zang_exception import ZangException

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.domain.enums.conference_status import ConferenceStatus

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
conferencesConnector = ConnectorFactory(configuration).conferencesConnector

# play audio to participant
try:
    participant = conferencesConnector.playAudioToParticipant(
        'ConferenceSid', 'ParticipantSid',
        'http://mydomain.com/audio.mp3')
    print(participant.duration)
except ZangException as ze:
    print(ze)
