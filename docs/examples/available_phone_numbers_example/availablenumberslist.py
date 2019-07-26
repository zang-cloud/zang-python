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
        contains="",                        #Any Integer will be accepted
        areaCode="",                        #Any area code will be accepted
        inRegion="ON",                      #Make sure region is in country
        inPostalCode="",                    #ie. m2j1x9 for Canada, 92010 for US
        page=0,                             #for if you want more options but have a smaller page
        pageSize=10)                        #smaller page size for better visibility
    print('\n',"Page: ",numbers.page,'\n',"Page Size: ",numbers.pageSize,'\n',"Total number of pages: ",numbers.total,'\n',"Starting Page Number: ",numbers.start,'\n',"Last Page Number: ",numbers.end)
    if numbers.elements:
        for item in numbers.elements:
            view = vars(item)
            print('\n')
            for item in view:
                print (item , ' : ' , view[item])
except ZangException as ze:
    print(ze)
