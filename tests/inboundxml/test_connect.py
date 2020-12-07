import unittest
from zang.inboundxml.elements.connect import Connect
from zang.domain.enums.http_method import HttpMethod
from zang.inboundxml.elements.agent import Agent


class TestConnect(unittest.TestCase):

    def test_init_with_required_values(self):
        expected = '<Connect></Connect>'
        assert Connect().xml == expected

    def test_init_add_element(self):
        agentId = '1234'
        agent = Agent(agentId)
        connect = Connect()
        connect.addElement(agent)
        expected = '<Connect><Agent>%s</Agent></Connect>' % agentId
        assert connect.xml == expected

    def test_init_remove_element_at_index(self):
        agentId = '1234'
        agent = Agent(agentId)
        connect = Connect()
        connect.addElement(agent)
        expected = '<Connect><Agent>%s</Agent></Connect>' % agentId
        assert connect.xml == expected
        connect.removeElementAtIndex(0)
        expected = '<Connect></Connect>'
        assert connect.xml == expected

    def test_remove_element_at_out_of_range_index(self):
        agentId = 'Hello from Zang!'
        agent = Agent(agentId)
        connect = Connect()
        connect.addElement(agent)
        index = len(connect._content)
        self.assertRaises(
            IndexError, lambda: connect.removeElementAtIndex(index))

    def test_init_with_optional_attributes(self):
        method = HttpMethod.GET
        connect = Connect(method=method)
        expected = '<Connect method="%s"></Connect>' % (method.value)
        assert connect.xml == expected

    def test_init_with_unsupported_attributes(self):
        self.assertRaises(TypeError, lambda: Connect(foo='bar'))

    def test_with_update_attributes(self):
        connect = Connect()
        action = "http://sample"
        connect.action = action
        expected = '<Connect action="%s"></Connect>' % (action)
        assert connect.xml == expected

    def test_udefinded_method_with_primitive_type(self):
        self.assertRaises(TypeError, lambda: Connect().addElement('bar'))

    def test_udefinded_method_with_base_node(self):
        self.assertRaises(AttributeError, lambda: Connect().url)


if __name__ == '__main__':
    unittest.main()
