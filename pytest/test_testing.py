# Pytest documentation: https://docs.pytest.org/en/stable/content.html

from testing import get_weather

def test_get_weather():
    assert get_weather(25) == "hot"
    assert get_weather(15) == "cold"
    assert get_weather(20) == "cold"  # Edge case

from testing import add, devide 
import pytest

def test_add():
    assert add(2, 3) == 5, "Adding 2 and 3 should return 5"
    assert add(-1, 1) == 0, "Adding -1 and 1 should return 0"
    assert add(0, 0) == 0, "Adding 0 and 0 should return 0"

def test_devide():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        devide(10, 0)

from testing import UserManager

@pytest.fixture
def user_manager():
    "Creates a fresh instance of UserManager before each test."
    return UserManager()

def test_add_user(user_manager):
    "Test adding a new user."
    assert user_manager.add_user("john_doe", "john@example.com") == True
    assert user_manager.get_user("john_doe") == "john@example.com"

def test_add_existing_user(user_manager):
    user_manager.add_user("john_doe", "john@example.com")
    with pytest.raises(ValueError):
        user_manager.add_user("john_doe", "another@example.com")