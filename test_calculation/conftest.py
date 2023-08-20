import pytest

@pytest.fixture
def csv_file():
    return 'csv file!!!'

def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os name')
