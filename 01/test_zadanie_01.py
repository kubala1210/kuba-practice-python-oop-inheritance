import pytest
from zadanie_01 import Admin, Guest

@pytest.fixture
def mock_user_data():
    return Admin('Kuba', 'secretpassword')

def test_get_display_name(mock_user_data):
    assert mock_user_data.get_display_name() == 'KUBA'

def test_authorize(mock_user_data):
    assert mock_user_data.authorize() == True

def test_has_access(mock_user_data):
    assert mock_user_data.has_access() == True

@pytest.fixture
def mock_invalid_user_data():
    return Admin('Kuba', 'pass')

def test_invalid_authorize(mock_invalid_user_data):
    with pytest.raises(ValueError):
        mock_invalid_user_data.authorize()

@pytest.fixture
def mock_guest_data():
    return Guest('Kuba', 'password')

def test_guest_authorize(mock_guest_data):
    assert mock_guest_data.authorize() == False