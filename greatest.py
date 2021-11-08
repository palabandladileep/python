import unittest
from great import greatest


class GreatTest(unittest.TestCase):
    def testgreat1(self):
        self.assertEqual(greatest(0, 0, 0), 0)

    def testgreat2(self):
        self.assertEqual(greatest(10, 20, 40), 40)

    def testgreat3(self):
        self.assertEqual(greatest(2, 3, "8"), None)
