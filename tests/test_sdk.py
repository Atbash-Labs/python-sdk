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


class TestGetKeyList(unittest.TestCase):
    def test_get_key_list_success(self):
        buyer = new_valid_buyer()
        key_list = buyer.get_key_list()

        self.assertEqual(len(key_list), 1)

    def test_key_list_added_key(self):
        buyer = new_valid_buyer()

        key_list = buyer.get_key_list()
        self.assertEqual(len(key_list), 1)

        _ = buyer.get_key()

        key_list = buyer.get_key_list()
        self.assertEqual(len(key_list), 2)

    def test_invalid_buyer(self):
        buyer = new_invalid_buyer()
        key_list = buyer.get_key_list()

        self.assertEqual(key_list, None)


class TestGetKey(unittest.TestCase):
    def test_get_key_success(self):
        buyer = new_valid_buyer()
        new_key = buyer.get_key()

        self.assertIsNotNone(new_key)

    def test_invalid_buyer(self):
        buyer = new_invalid_buyer()
        new_key = buyer.get_key()

        self.assertEqual(new_key, None)
