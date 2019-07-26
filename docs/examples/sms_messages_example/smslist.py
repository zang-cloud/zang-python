from datetime import date

from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'


configuration = Configuration(sid, authToken, url=url)
smsMessagesConnector = ConnectorFactory(configuration).smsMessagesConnector

# list sms messages
try:
    
    smsMessages = smsMessagesConnector.listSmsMessages(
        dateSentGte=date(2019, 6, 1), dateSentLt=date(2019, 6, 30))
    print('You have ',smsMessages.total,' messages in the set date')
    for smsMessage in smsMessages.elements:
        view = vars(smsMessages)
        print('\n')
        for item in view:
            print (item , ' : ' , view[item])
        viewMessage = smsMessagesConnector.viewSmsMessage(smsMessage.sid)
        view = vars(smsMessage)
        print('\n')
        for item in view:
            print (item , ' : ' , view[item])
except ZangException as e:
    print(e)

    """
        Text messages sent to and from Zang phone numbers are represented with.

        :param to: (optional) Lists all SMS messages sent to this number.
        :param from_: (optional) Lists all SMS messages sent from this number.
        :type dateSentGte: (optional) Filter by date sent greater or equal then
        :type dateSentLt: (optional) Filter by date sent less than
        :param pageSize: (optional) Used to specify the amount of list items
            to return per page.

        :type to: (optional) str
        :type from_: (optional) str
        :type dateSentGte: (optional) datetime.date
        :type dateSentLt: (optional) datetime.date
        :type page: (optional) int
        :type pageSize: (optional) int

        
        """
