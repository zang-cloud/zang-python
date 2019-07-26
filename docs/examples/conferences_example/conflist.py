from datetime import date
from zang.exceptions.zang_exception import ZangException

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.domain.enums.conference_status import ConferenceStatus

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
conferencesConnector = ConnectorFactory(configuration).conferencesConnector


# list conferences
try:
    fromDate = date(2018, 12, 31)
    toDate = date(2019, 12, 31)
    conferences = conferencesConnector.listConferences(
        status=ConferenceStatus.COMPLETED,
        dateCreatedGte=fromDate,
        dateCreatedLt=toDate,
        dateUpdatedGte=fromDate,
        dateUpdatedLt=toDate,
        page=0,
        pageSize=33)
    if conferences and conferences.elements:
        for conference in conferences.elements:
            view = vars(conference)
            print('\n')
            for item in view:
                print (item , ' : ' , view[item])
    else:
        print("no conference to list!")
except ZangException as ze:
    print(ze)

