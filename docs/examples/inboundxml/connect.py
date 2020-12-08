from zang.inboundxml import Response, Connect, Agent

from zang.domain.enums.http_method import HttpMethod

connect = Connect("http://example.com/example-callback-url/say?example=simple.xml",
                method=HttpMethod.GET)

agent = Agent("1234")

connect.addElement(agent)

response = Response()
response.addElement(connect)

print(response.xml)
