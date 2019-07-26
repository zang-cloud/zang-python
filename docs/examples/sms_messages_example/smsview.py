from datetime import date

from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'


configuration = Configuration(sid, authToken, url=url)
smsMessagesConnector = ConnectorFactory(configuration).smsMessagesConnector

# view sms message
try:
    smsMessage = smsMessagesConnector.viewSmsMessage('SmsSid')
    view = vars(smsMessage)
    for item in view:
        print (item , ' : ' , view[item])
    
except ZangException as e:
    print(e)
    
'''
Parameters:

api_version
The Api Version being used.

sid
An alphanumeric string identifying this resource.

account_sid:
An alphanumeric string identifying the account this call occurred through.

date_created
The date the SMS resource was created.

date_updated
The date the SMS resource was last updated.

date_sent
The date the SMS was sent.

to
The date the SMS was sent.

from
The number that sent the SMS message.

body
Text of the SMS message sent or received. May be up to 160 characters in length.

status
Status of the SMS: sent, sending, queued, or failed.

direction
Specifies the direction of the SMS: messages from REST API are “outbound-api”, messages from incoming phone numbers to Avaya CPaaS are “incoming”, messages from InboundXML initiated during an outbound call are “outbound-call”, and messages from InboundXML initiated via an sms reply are “outbound-reply”.

price
Cost of the SMS.

uri
The Uniform Resource Identifier to this resource
'''
