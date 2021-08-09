import pytest

MOCK_DICTIONARY ={
    "first_name": "Odasys",
    "last_name": "soberanes",
    "activity": 1,
    "age" : 100
}

def test_dictionary_has_valid_age():
    assert isinstance(MOCK_DICTIONARY["age"], int)

def username():
    assert MOCK_DICTIONARY.get("username")

