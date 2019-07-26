from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.log_level import LogLevel


from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
notificationsConnector = ConnectorFactory(configuration).notificationsConnector

# view notification
try:
    notification = notificationsConnector.viewNotification(
        "NotificationSid")
    view = vars(notification)
    print('\n')
    for item in view:
        print (item , ' : ' , view[item])
except ZangException as ze:
    print(ze)
