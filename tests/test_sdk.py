import pytest
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


def test_get_key_list_success():
    buyer = new_valid_buyer()
    key_list = buyer.get_key_list()

    assert len(key_list) == 1


def test_key_list_added_key():
    buyer = new_valid_buyer()

    key_list = buyer.get_key_list()
    assert len(key_list) == 1

    _ = buyer.get_key()

    key_list = buyer.get_key_list()
    assert len(key_list) == 2


def test_invalid_buyer_for_key_list():
    buyer = new_invalid_buyer()
    key_list = buyer.get_key_list()

    assert key_list == None


def test_get_key_success():
    buyer = new_valid_buyer()
    new_key = buyer.get_key()

    assert new_key != None


def test_invalid_buyer_for_new_key():
    buyer = new_invalid_buyer()
    new_key = buyer.get_key()

    assert new_key == None
