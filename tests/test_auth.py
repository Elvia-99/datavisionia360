import pytest
from utils.auth import login_user

def test_login_success():
    """Debe autenticar usuario válido."""
    user = login_user("admin", "1234")
    assert user is not None
    assert user["username"] == "admin"

def test_login_failure():
    """Debe rechazar credenciales incorrectas."""
    user = login_user("admin", "wrongpass")
    assert user is None

