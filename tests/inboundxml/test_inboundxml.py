import unittest
from zang.inboundxml.elements.pause import Pause


class TestInboundxml(unittest.TestCase):

    def test_pause(self):
        pause = Pause()
        def addPause():
            pause.addElement('text')

        assert pause.xml == '<Pause/>'
        self.assertRaises(TypeError, addPause)

if __name__ == '__main__':
    unittest.main()


