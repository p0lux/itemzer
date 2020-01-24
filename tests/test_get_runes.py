import unittest
from itemzer.request_page import make_request


class MyTestCase(unittest.TestCase):
    # Test if status_code is not 404
    def test_request_web(self):
        self.assertIsNot(make_request('http://www.op.gg/champion/ekko/statistics/top'), '404', 'website unavailable')
        self.assertIsNot(make_request('https://champion.gg/champio/aatroxp'), '404', 'website unavailable')
        self.assertIsNot(make_request('https://lolcounter.com/champions/draven'), '404', 'website unavailable')


if __name__ == '__main__':
    unittest.main()
