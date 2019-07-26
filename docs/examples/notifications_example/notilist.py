from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.log_level import LogLevel


from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
notificationsConnector = ConnectorFactory(configuration).notificationsConnector

# list notifications
try:
    notifications = notificationsConnector.listNotifications(
        log=2, page=0, pageSize=33)
    view = vars(notifications)
    print('\n')
    for item in view:
        print(item , ' : ' , view[item])
    if notifications and notifications.elements:
        for notification in notifications.elements:
            view = vars(notification)
            print('\n')
            for item in view:
                print (item , ' : ' , view[item])

except ZangException as ze:
    print(ze)

'''
QUERY PARAMS
Log:
Specifies that only notifications with the given log level value should be listed. Allowed values are 1,2 or 3, where 2=INFO, 1=WARNING, 0=ERROR.

Page:
Used to return a particular page within the list.

PageSize:
Used to specify the amount of list items to return per page.
'''
