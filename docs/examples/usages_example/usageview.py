from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.domain.enums.product import Product

from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
usagesConnector = ConnectorFactory(configuration).usagesConnector


# view usage
try:
    usage = usagesConnector.viewUsage('UsageSid')
    view = vars(usage)
    for item in view:
        print (item , ' : ' , view[item])
except ZangException as ze:
    print(ze)

'''
Response Parameters:

sid
An alphanumeric string identifying this resource.

product
The product or feature used.

product_id
An integer identifying this product. You can see the full list under List Usage.

day
The day of the usage.

month
The month of the usage.

year
The year of the usage.

quantity
The quantity of the usage.

average_cost
The average cost of the usage.

total_cost
The total cost of the usage.

uri
The URL to this resource.
'''
