import pytest
from fortress_sdk import Buyer


@pytest.fixture
def valid_buyer():
    api_key = "buyer_key"
    ip_addr = "127.0.0.1"
    buyer = Buyer(api_key, ip_addr)
    return buyer


@pytest.fixture
def invalid_buyer():
    api_key = "invalid_buyer_key"
    ip_addr = "127.0.0.1"
    buyer = Buyer(api_key, ip_addr)
    return buyer


def test_get_key_list_success(valid_buyer):
    key_list = valid_buyer.get_key_list()

    assert len(key_list) == 1


def test_key_list_added_key(valid_buyer):
    key_list = valid_buyer.get_key_list()
    assert len(key_list) == 1

    _ = valid_buyer.get_key()

    key_list = valid_buyer.get_key_list()
    assert len(key_list) == 2


def test_invalid_buyer_for_key_list(invalid_buyer):
    key_list = invalid_buyer.get_key_list()

    assert key_list == None


def test_get_key_success(valid_buyer):
    new_key = valid_buyer.get_key()

    assert new_key != None


def test_invalid_buyer_for_new_key(invalid_buyer):
    new_key = invalid_buyer.get_key()

    assert new_key == None


def test_query_success(valid_buyer):
    sql_query = "select count(*) as numpeople from public.condition_era_death"
    result, accuracy = valid_buyer.query(query=sql_query)

    assert result != None
    assert accuracy != ""


def test_query_history(valid_buyer):
    sql_query = "select count(*) as numpeople from public.condition_era_death"
    _ = valid_buyer.query(query=sql_query)
    sql_query = "select count(*) as numpeople from public.condition_era_death"
    _ = valid_buyer.query(query=sql_query)

    assert len(valid_buyer.all_queries) == 2

    sql_query = "select count(*) as numpeople from public.condition_era_death"
    _ = valid_buyer.query(query=sql_query)

    assert len(valid_buyer.all_queries) == 3
