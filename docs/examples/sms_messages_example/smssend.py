from datetime import date

from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'


configuration = Configuration(sid, authToken, url=url)
smsMessagesConnector = ConnectorFactory(configuration).smsMessagesConnector

# send sms message
try:
    smsMessage = smsMessagesConnector.sendSmsMessage(
        to='e164',
        body='Hello from Zang!',
        from_='e164')
    view = vars(smsMessage)
    print('\n')
    for item in view:
        print (item , ' : ' , view[item])
except ZangException as e:
    print(e)
