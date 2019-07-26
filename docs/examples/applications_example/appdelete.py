from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.domain.enums.http_method import HttpMethod

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
applicationsConnector = ConnectorFactory(configuration).applicationsConnector


# delete application
try:
    application = applicationsConnector.deleteApplication('PlaceApplicationSID')
    application = applicationsConnector.listApplications(
        'TestApplication', 0, 33)
    print("Deleted!")
    print("There are now a total of", application.total, "application(s).")

except ZangException as ze:
    print(ze)
