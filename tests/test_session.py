import pytest
from game import SessionGame


@pytest.fixture
def get_session_fixture():
    return SessionGame('player_1', 'player_2')


def test_something_that_involves_user_input(get_session_fixture):
    session = get_session_fixture
    assert all(session.get_session())


def test_get_session_player(get_session_fixture):
    session = get_session_fixture
    assert session.get_session_player().name == 'player_1'
