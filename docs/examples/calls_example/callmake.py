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


try:
    call = callsConnector.makeCall(
        to='e164',
        from_='e164',
        url='http://zang.io/ivr/welcome/call',
        method=HttpMethod.GET,
        fallbackUrl='',
        fallbackMethod=HttpMethod.POST,
        statusCallback='',
        statusCallbackMethod=HttpMethod.GET,
        heartbeatUrl='',
        heartbeatMethod=HttpMethod.GET,
        forwardedFrom='',
        playDtmf='',
        timeout=122,
        hideCallerId=False,
        record=False,
        recordCallback='',
        recordCallbackMethod=HttpMethod.GET,
        transcribe=False,
        transcribeCallback='',
        straightToVoicemail=False,
        ifMachine=IfMachine.REDIRECT,
        ifMachineUrl='',
        ifMachineMethod=HttpMethod.GET,
        sipAuthUsername='username',
        sipAuthPassword='password')
    view = vars(call)
    print('\n')
    for item in view:
        print (item , ' : ' , view[item])
except ZangException as ze:
    print(ze)
