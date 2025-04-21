import pytest
from zadanie_02 import User, Admin, Guest

@pytest.fixture
def mock_user_data():
    return Admin('Anna'), Guest('Kuba'), User('Tomek')

def test_user_counter(mock_user_data):
    assert User.total_users == 3

@pytest.fixture
def mock_admin_data():
    return Admin('Michał')

def test_name_printer(mock_admin_data):
    assert mock_admin_data.name == 'Michał'