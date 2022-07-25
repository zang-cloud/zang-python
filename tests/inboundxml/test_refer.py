import unittest
from zang.inboundxml.elements.refer import Refer
from zang.domain.enums.http_method import HttpMethod
from zang.inboundxml.elements.sip import Sip


class TestRefer(unittest.TestCase):

    def test_init_with_required_values(self):
        expected = '<Refer></Refer>'
        assert Refer().xml == expected

    def test_init_with_arguments(self):
        text = 'sip:username@example.com'
        refer = Refer(address=text)
        expected = '<Refer>%s</Refer>' % text
        assert refer.xml == expected

    def test_init_add_element(self):
        text = 'username@example.com'
        sip = Sip(text)
        refer = Refer()
        refer.addElement(sip)
        expected = '<Refer><Sip>%s</Sip></Refer>' % text
        assert refer.xml == expected

    def test_init_remove_element_at_index(self):
        text = 'Hello from Avaya CPaaS!'
        sip = Sip(text)
        refer = Refer()
        refer.addElement(sip)
        expected = '<Refer><Sip>%s</Sip></Refer>' % text
        assert refer.xml == expected
        refer.removeElementAtIndex(0)
        expected = '<Refer></Refer>'
        assert refer.xml == expected

    def test_remove_element_at_out_of_range_index(self):
        text = 'Hello from Avaya CPaaS!'
        sip = Sip(text)
        refer = Refer()
        refer.addElement(sip)
        index = len(refer._content)
        self.assertRaises(
            IndexError, lambda: refer.removeElementAtIndex(index))

    def test_init_with_optional_attributes(self):
        method = HttpMethod.GET
        refer = Refer(method=method)
        expected = '<Refer method="%s"></Refer>' % (method.value)
        assert refer.xml == expected

    def test_init_with_unsupported_attributes(self):
        self.assertRaises(TypeError, lambda: Refer(foo='bar'))

    def test_with_update_attributes(self):
        refer = Refer()
        timeout = 0
        refer.timeout = 0
        expected = '<Refer timeout="%s"></Refer>' % (timeout)
        assert refer.xml == expected

    def test_udefinded_method_with_primitive_type(self):
        self.assertRaises(TypeError, lambda: Refer().addElement(0.5))

    def test_udefinded_method_with_base_node(self):
        self.assertRaises(AttributeError, lambda: Refer().url)


if __name__ == '__main__':
    unittest.main()
