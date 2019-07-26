from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.domain.enums.product import Product

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
usagesConnector = ConnectorFactory(configuration).usagesConnector


# list usages
try:
    product = Product.ordinal(Product.OUTBOUND_CALL)
    usages = usagesConnector.listUsages(
        #product=1,
        year=2019,
        month=6,
        pageSize=100)
    total = 0.0
    for usage in usages.elements:
        view = vars(usages)
        for item in view:
            print (item , ' : ' , view[item])
        viewUsage = usagesConnector.viewUsage(usage.sid)
        view = vars(viewUsage)
        print('\n')
        for item in view:
            print (item , ' : ' , view[item])
except ZangException as ze:
    print(ze)

'''
QUERY PARAMS
Day:
Filters usage by day of month. If no month is specified then defaults to current month. Allowed values are integers between 1 and 31 depending on the month. Leading 0s will be ignored.

Month:
Filters usage by month. Allowed values are integers between 1 and 12. Leading 0s will be ignored.

Year:
Filters usage by year. Allowed values are valid years in integer form such as "2014".

Product:
Filters usage by a specific “product” of Avaya CPaaS. Each product is uniquely identified by an integer. For example: Product=1, would return all outbound call usage. The integer assigned to each product is listed below.

Page:
Used to return a particular page within the list.

PageSize:
Used to specify the amount of list items to return per page.

Product  Product Code

Outbound Call 1

Inbound Call 2

Outbound SMS 3

Inbound SMS 4

Outbound SIP 5

Inbound SIP 6

Recording 7

Recurring DID 8

Recurring DID (Premium) 9

Transcription (Auto) 12

Transcription (Hybrid) 14

Recurring Inbound Channel 17

Inbound Call (Channel) 18

CNAM Dip 19

Carrier Lookup 20

Outbound Call (Spoofed) 21

Inbound Call (Channel Overage) 22

Recurring DID Unblock 23

Inbound Call Unblocked 24

Inbound Call Forwarded From 25
'''
