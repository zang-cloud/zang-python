from datetime import date
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.call_status import CallStatus
from zang.domain.enums.http_method import HttpMethod
from zang.domain.enums.if_machine import IfMachine
from zang.domain.enums.end_call_status import EndCallStatus
from zang.domain.enums.audio_direction import AudioDirection
from zang.domain.enums.recording_file_format import RecordingFileFormat
from zang.domain.enums.recording_audio_direction import RecordingAudioDirection
from zang.domain.enums.transcribe_quality import TranscribeQuality


from zang.exceptions.zang_exception import ZangException

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'


configuration = Configuration(sid, authToken, url=url)
callsConnector = ConnectorFactory(configuration).callsConnector



# list calls
try:
    calls = callsConnector.listCalls(
        #to='+',
        #from_='+',
        #status=CallStatus.COMPLETED,
        #startTimeGte=date(2018, 12, 31),
        #startTimeLt=date(2019, 12, 31),
        #page=0,
        pageSize=10)
    print(calls.total)
except ZangException as ze:
    print(ze)
