import pytest
import LogicLayer.LogicController as logic


@pytest.fixture()
def clean_db():
    logic.deleteallusers()
    logic.deleteallsongs()


@pytest.fixture()
def set_user_in_db():
    user = {
        "user_name": "Linda",
        "user_password": "4321"
    }
    logic.deleteallusers()
    logic.adduser(user)


@pytest.fixture()
def set_song_in_db():
    logic.deleteallsongs()
    logic.addsong("Rap", "1999", "2Pac", "Dear Mama")


@pytest.fixture()
def set_user_playlist_and_song_in_db():
    logic.deleteallusers()
    logic.deleteallsongs()
    user = {
        "user_name": "Linda",
        "user_password": "4321"
    }
    logic.adduser(user)
    logic.addplaylist("Linda", "4321", "Summer22")
    logic.addsong("Rap", "2003", "Eminem", "Lose yourself")


@pytest.fixture()
def set_user_and_song_in_playlist():
    logic.deleteallusers()
    logic.deleteallsongs()
    user = {
        "user_name": "Linda",
        "user_password": "4321"
    }
    logic.adduser(user)
    logic.addplaylist("Linda", "4321", "Summer22")
    logic.addsong("Rap", "2003", "Eminem", "Lose yourself")
    logic.addsongtoplaylist("Summer22", "Lose yourself", "Linda", "4321")
