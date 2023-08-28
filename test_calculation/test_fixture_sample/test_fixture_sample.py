# test_fixture_sample.py

import pytest

from users_db import Users

@pytest.fixture # これがフィクスチャ
def db():
    users = Users()
    users.insert('Bob', 10)
    users.insert('Alice', 12)
    return users

# dbフィクスチャを利用するテストケース
def test_one(db):
    assert db.get(1)['name'] == 'Bob'


# フィクスチャは複数のテストケースで共有できる
def test_two(db):
    assert db.get(2)['name'] == 'Alice'


# クラスベースのテストでも利用できる
class TestUsers:
    def test_one(self, db):
        assert db.get(1)['name'] == 'Bob'
