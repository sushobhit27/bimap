import pytest

from ..bimap import Bimap, MultiBimap


@pytest.fixture
def bm():
    bm = Bimap()
    bm.left[1] = 'a'
    bm.left[2] = 'b'
    bm.left[3] = 'c'
    return bm


def test_basic(bm):
    assert bm.left[2] == 'b'
    assert bm.right['c'] == 3


def test_insert(bm):
    bm.right['d'] = 4
    assert bm.left[4] == 'd'
    assert bm.right['d'] == 4


def test_overwrite(bm):
    #import pdb;pdb.set_trace()
    bm.left[2] = 'xyz'
    assert bm.left[2] == 'xyz'
    assert bm.right['xyz'] == 2


def test_keys(bm):
    assert list(bm.left.keys()) == [1, 2, 3]
    assert list(bm.right.keys()) == ['a', 'b', 'c']


def test_keys_values(bm):
    assert list(bm.left.keys()) == list(bm.right.values())
    assert list(bm.left.values()) == list(bm.right.keys())


def test_values(bm):
    assert list(bm.left.values()) == ['a', 'b', 'c']
    assert list(bm.right.values()) == [1, 2, 3]


def test_keys_after_insert(bm):
    bm.right['d'] = 4
    assert list(bm.left.keys()) == [1, 2, 3, 4]
    assert list(bm.right.keys()) == ['a', 'b', 'c', 'd']


def test_values_after_insert(bm):
    bm.right['d'] = 4
    assert list(bm.left.values()) == ['a', 'b', 'c', 'd']
    assert list(bm.right.values()) == [1, 2, 3, 4]


def test_keys_values_after_insert(bm):
    bm.right['d'] = 4
    assert list(bm.left.keys()) == list(bm.right.values())
    assert list(bm.left.values()) == list(bm.right.keys())


def test_keys_after_overwrite(bm):
    print(list(bm.left.keys()))
    print(list(bm.left.values()))
    #import pdb;pdb.set_trace()
    bm.left[2] = 'xyz'
    bm.left[3] = 'sush'
    bm.right['a'] = 786
    print(list(bm.left.keys()))
    print(list(bm.left.values()))
    print(list(bm.right.keys()))
    print(list(bm.right.values()))
    assert sorted(list(bm.left.keys())) == sorted([786, 2, 3])
    assert sorted(list(bm.right.keys())) == sorted(['a', 'xyz', 'sush'])


def test_keys_values_after_modify(bm):
    bm.left[2] = 'xyz'
    assert list(bm.left.keys()) == list(bm.right.values())
    assert list(bm.left.values()) == list(bm.right.keys())

