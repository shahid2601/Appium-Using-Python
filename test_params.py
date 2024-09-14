import pytest


def getData():
    return [
        ('shahid', '12345'),
        ('chris', '1234')
    ]

@pytest.mark.parametrize("username, password", getData())

def test_login(username, password):
    print("userName====", username, "------", "password====", password)