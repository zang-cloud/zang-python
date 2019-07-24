from zang.exceptions.zang_exception import ZangException

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.domain.enums.available_number_type import AvailableNumberType

from docs.examples.credentials import sid, authToken
url = 'http://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
availablePhoneNumbersConnector = ConnectorFactory(
    configuration).availablePhoneNumbersConnector

try:
    numbers = availablePhoneNumbersConnector.listAvailablePhoneNumbers(
        country="CA",                       #ie. CA for Canada; US for the States
        type_=AvailableNumberType.LOCAL,    #LOCAL or TOLLFREE
        contains="",                        
        areaCode="",
        inRegion="",
        inPostalCode="m2j1x9",              #ie. m2j1x9 for Canada, 92010 for US
        page=0,
        pageSize=50)
    #for i in range(len(numbers._available_phone_numbers)):
    print  (numbers._available_phone_numbers)
except ZangException as ze:
    print(ze)
