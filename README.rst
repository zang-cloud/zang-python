zang-python
==========

This python package is an open source tool built to simplify interaction with
the `Zang <https://www.zang.io>`_ telephony platform. Zang makes adding voice
and SMS to applications fun and easy.

For more information about Zang, please visit: 
`Zang Cloud <https://www.zang.io/products/cloud>`_

To read the official documentation, please visit: `Zang Docs <https://docs.zang.io/aspx/docs>`_.


Installation
============

Clone the repo, and install via ``pip``:

.. code-block:: bash

    $ git clone git@github.com:zang-cloud/zang-python.git
    $ cd zang-python
    $ pip install -e .

.. code-block:: bash

Usage
======

REST
----

See the `Zang REST API documentation <https://docs.zang.io/aspx/rest>`_
for more information.

Send SMS Example
----------------

.. code-block:: python

    from datetime import date
    from zang import ZangException, Configuration, ConnectorFactory

    sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    url = 'https://api.zang.io/v2'

    configuration = Configuration(sid, authToken, url=url)
    smsMessagesConnector = ConnectorFactory(configuration).smsMessagesConnector

    # send sms message
    try:
        smsMessage = smsMessagesConnector.sendSmsMessage(
            to='(XXX) XXX-XXXX',
            body='Hello from Zang!',
            from_='(XXX) XXX-XXXX')
        print(smsMessage)
    except ZangException as ze:
        print(ze)
        
.. code-block:: python

Configuration
-------------

First a configuration object must be created by using ``Configuration`` class.

Normally you'll want to just enter your Zang Platform Account ``sid``
and ``authToken``, but you can also define a base API URL.

Base API URL is defined in constants.py with following defaults:

.. code-block:: python

    BASE_URL = 'https://api.zang.io'
    API_VERSION = 'v2'

.. code-block:: python

The base API URL and api version for US(new) and EU deployments are:
US: https://api-us.cpaas.avayacloud.com/v2
EU: https://api-eu.cpaas.avayacloud.com/v2

These values can be changed in constants.py. For example, if we need
to run our code snippet in EU deployment, code has to be changed as below:

.. code-block:: python

    BASE_URL = 'https://api-eu.cpaas.avayacloud.com'
    API_VERSION = 'v2'

.. code-block:: python

Next you'll have to create a connector by using ``ConnectorFactory``.
This can be done in multiple ways. The usual way is to instantiate
``ConnectorFactory``, pass the configuration object to the factory and have
it instantiate ``ZangConnector`` objects:

.. code-block:: python

    callsConnector = ConnectorFactory(configuration).callsConnector
    callsConnector.makeCall(...)

.. code-block:: python


Request parameters
------------------

Request parameters are passed as parameters to connector object methods as
shown previously. All methods use the Account ``sid`` parameter specified 
in the configuration automatically:

.. code-block:: python

    usagesConnector = ConnectorFactory(configuration).usagesConnector
    # Account sid from configuration used automatically
    usage = usagesConnector.viewUsage('{UsageSid}')

.. code-block:: python


Methods usually have optional parameters. To specify an optional parameter,
use ``parameterName=value`` in a method call e.g.:

.. code-block:: python

    call = callsConnector.makeCall(
        '+123456',
        '+654321',
        'TestUrl',
        method=HttpMethod.GET,
        fallbackUrl='FallbackUrl')

.. code-block:: python


Response data
-------------

The received data can be an object, e.g.:

.. code-block:: python

    usagesConnector = ConnectorFactory(configuration).usagesConnector
    usage = usagesConnector.viewUsage('{UsageSid}')
    print(usage.totalCost)

.. code-block:: python

Or a list of objects in which case the list is iterable, e.g.:

.. code-block:: python

    usagesConnector = ConnectorFactory(configuration).usagesConnector
    usages = usagesConnector.listUsages(
        product=Product.ordinal(Product.OUTBOUND_CALL),
        year=2017,
        month=2,
        pageSize=100)
    if usages and usages.elements:
        for usage in usages.elements:
            print(usage.totalCost)

.. code-block:: python


InboundXML
==========

InboundXML is an XML dialect which enables you to control phone call flow.
For more information please visit the `Zang InboundXML documentation
<https://docs.zang.io/aspx/inboundxml>`_.

<Say> Example
-------------

.. code-block:: python

    from zang.inboundxml import Response, Say

    # enums
    from zang.inboundxml import Voice, Language

    say = Say("Welcome to Zang!",
              language=Language.EN,
              voice=Voice.FEMALE,
              loop=3)

    response = Response()
    response.addElement(say)

    print(response.xml)

.. code-block:: python

will render

.. code-block:: xml
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Response>
        <Say loop="3" voice="female" language="en">Welcome to Zang!</Say>
    </Response>

.. code-block:: xml
