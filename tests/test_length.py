import unittest
from superawesomepackage.lib import try_me

class TestDistanceMethods(unittest.TestCase):

    def test_type_return(self):
        self.assertEqual(len(try_me(42)), 210, f'{try_me(42)} != 210')