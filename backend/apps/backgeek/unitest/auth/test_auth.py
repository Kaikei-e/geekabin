import os

from authenticator.auth import verify_password
from dotenv import load_dotenv

load_dotenv()


def test_verify_password():
    assert verify_password('huge', os.environ['HASHED_PASS'])


def test_get_password_hash():
    assert False


def test_get_user():
    assert False


def test_oath_keeper():
    assert False


def test_create_access_token():
    assert False


def test_get_current_user():
    assert False


def test_get_current_active_user():
    assert False


def test_login_access_token():
    assert False


def test_token():
    assert False


def test_token_data():
    assert False


def test_user():
    assert False


def test_user_in_db():
    assert False
