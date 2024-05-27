import unittest
from name import phone_model

class Phone(unittest.TestCase):
    def texno_park(self):
        honey = phone_model('iphone 15 pro max','apple',1499)
        self.assertEqual(honey,'Apple: iphone 15 pro max')

unittest.main()

