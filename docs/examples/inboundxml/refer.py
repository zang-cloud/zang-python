from zang.inboundxml import Response, Refer, Sip

from zang.domain.enums.http_method import HttpMethod

refer = Refer(
                action="https://example.com/actionURL",
                method=HttpMethod.POST,
                timeout=180,
                callbackUrl="https://example.com/callbackURL",
                callbackMethod=HttpMethod.POST,
                )

sip = Sip("username@example.com",
          username="username",
          password="pass",)

refer.addElement(sip)

response = Response()
response.addElement(refer)

print(response.xml)
