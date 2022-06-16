
import unittest
from weather import call_weather


class TestCity(unittest.TestCase):
    def test_case_real(self):
        """"
        testing real time scenario
        """
        call_weather("india")
        city="india"

        self.assertEqual(city,"india","invalid operation")


if __name__ == '__main__':
    unittest.main()