"""Tests for Phonebook class."""

import pytest


def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "1234")
    assert "1234" == phonebook.lookup("Bob")


def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob", "1234")
    assert "Bob" in phonebook.names()


def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")


def test_empty_phonebook_is_consistent(phonebook):
    assert phonebook.is_consistent()


@pytest.mark.parametrize("entry1,entry2,is_consistent", [
    (("Bob", "12345"), ("Anna", "01234"), True),
    (("Bob", "12345"), ("Sue", "12345"), False),
    (("Bob", "12345"), ("Sue", "123"), False),
])
def test_is_consistent(phonebook, entry1, entry2, is_consistent):
    phonebook.add(*entry1)
    phonebook.add(*entry2)
    assert phonebook.is_consistent() == is_consistent


@pytest.mark.skip("Work in process on new feature")
def test_some_new_feature():
    assert False # test should fail!