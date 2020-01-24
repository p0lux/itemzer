import unittest
from itemzer.request_page import return_content_bs, return_content_lol_counter, return_content_op


class MyTestCase(unittest.TestCase):
    # Test if status_code is not 404
    def test_request_bs(self):
        self.assertIsNot('404', return_content_bs)


if __name__ == '__main__':
    unittest.main()
