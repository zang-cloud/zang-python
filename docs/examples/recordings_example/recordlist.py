from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.recording_audio_direction import RecordingAudioDirection
from zang.domain.enums.recording_file_format import RecordingFileFormat
from zang.domain.enums.transcribe_quality import TranscribeQuality


from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
recordingsConnector = ConnectorFactory(configuration).recordingsConnector


# list recordings
try:
    recording = recordingsConnector.listRecordings('CallSid')
    view = vars(recording)
    for item in view:
        print (item , ' : ' , view[item])
    for listrecord in recording.elements:
        records = recordingsConnector.viewRecording(listrecord.sid)
        view = vars(records)
        print('\n')
        for item in view:
            print (item , ' : ' , view[item])
except ZangException as ze:
    print(ze)
    
    
