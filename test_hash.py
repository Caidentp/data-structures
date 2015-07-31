import pytest

from hashtable import HashTable


@pytest.fixture()
def word_list():
    with open('/usr/share/dict/words') as fh:
        words = fh.read()
    words = words.split('\n')
    return words


def test_init_default():
    foo = HashTable()
    assert foo.table_size == 1024
    assert len(foo.hashtable) == 1024


def test_init_set_size():
    foo = HashTable(size=4096)
    assert foo.table_size == 4096
    assert len(foo.hashtable) == 4096


def test_len():
    foo = HashTable()
    empty_len = len(foo)
    stuff = [('a', 'a'), ('b', 'b'), ('c', 'c')]
    more = [('d', 'd'), ('e', 'e')]
    foo.hashtable[0].extend(stuff)
    foo.hashtable[500].extend(more)
    filled_len = len(foo)
    assert empty_len == 0
    assert filled_len == 5


def test_set_wrong_type():
    foo = HashTable()
    with pytest.raises(TypeError):
        foo.set(898, [838])


def test_get_missing_key():
    foo = HashTable()
    with pytest.raises(KeyError):
        foo.get('bar')


def test_set_and_get_word_list(word_list):
    foo = HashTable()
    words = word_list
    for word in words:
        foo.set(word, word)
    for word in words:
        value = foo.get(word)
        assert word == value
