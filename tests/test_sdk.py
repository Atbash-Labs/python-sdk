import unittest
from fortress_sdk import Buyer


def new_valid_buyer():
    api_key = "buyer_key"
    ip_addr = "127.0.0.1"
    buyer = Buyer(api_key, ip_addr)
    return buyer


def new_invalid_buyer():
    api_key = "invalid_buyer_key"
    ip_addr = "127.0.0.1"
    buyer = Buyer(api_key, ip_addr)
    return buyer


class TestGetKey(unittest.TestCase):
    def test_get_key_success(self):
        buyer = new_valid_buyer()
        new_key = buyer.get_key()

        self.assertIsNotNone(new_key)

    def test_invalid_buyer(self):
        buyer = new_invalid_buyer()
        new_key = buyer.get_key()

        self.assertEqual(new_key, None)
