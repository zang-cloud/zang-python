from datetime import date

from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'


configuration = Configuration(sid, authToken, url=url)
mmsMessagesConnector = ConnectorFactory(configuration).mmsMessagesConnector

# send sms message
try:
    mmsMessage = mmsMessagesConnector.sendMmsMessage(
        to='(XXX) XXX-XXXX',
        mediaUrl="https://gph.is/g/4DedxMn",
        body='This is MMS sent from Zang',
        from_='(XXX) XXX-XXXX',
        statusCallback='callback.url')
    view = vars(mmsMessage)
    print('\n')
    for item in view:
        print (item , ' : ' , view[item])
except ZangException as e:
    print("in exception")
    print(e)
