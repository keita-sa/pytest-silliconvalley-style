import pytest

from prime import is_prime

# パラメータ化したテスト
@pytest.mark.parametrize(('number', 'expected'), [ # スペル注意
    (1, False), # タプルをリストの要素としない
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (8, False),
    (9, False),
    (10, False),
])
def test_is_prime(number, expected):
    assert is_prime(number) == expected