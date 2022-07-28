import LogicLayer.LogicController as logic


def test_add_user_successfully(clean_db):
    user = {
        "user_name": "Linda",
        "user_password": "4321"
    }
    status, result = logic.adduser(user)
    data = result['data']
    message = result['message']
    assert data == "Linda" and message == "OK" and status == 200


def test_add_existing_user(set_user_in_db):
    # user in db = "user_name":"Linda", "user_password": "4321"
    user = {
        "user_name": "Linda",
        "user_password": "4321"
    }
    status, result = logic.adduser(user)
    message = result['error']
    assert message == "user with name Linda already exists." and status == 200


def test_get_user_successfully(set_user_in_db):
    # user in db = "user_name":"Linda", "user_password": "4321"
    status, result = logic.getuser("Linda")
    message = result['message']
    username = result['data']['user_name']
    assert username == "Linda" and message == "OK" and status == 200


def test_get_user_not_exist(clean_db):
    status, result = logic.getuser("Linda")
    message = result['error']
    assert message == "user Linda does not exist" and status == 200


def test_add_playlist_successfully(set_user_in_db):
    # user in db = "user_name":"Linda", "user_password": "4321"
    status, result = logic.addplaylist("Linda", "4321", "Summer22")
    actualname = result['data']
    expectedname = "Summer22"
    assert actualname == expectedname


def test_add_playlist_to_non_existing_user(clean_db):
    status, result = logic.addplaylist("Avi", "1234", "MyPlaylist")
    message = result['error']
    assert message == "the user Avi does not exist" and status == 200


def test_add_playlist_wrong_password(set_user_in_db):
    # user in db = "user_name":"Linda", "user_password": "4321"
    status, result = logic.addplaylist("Linda", "1111", "Summer22")
    message = result['error']
    assert message == "either the user name or the password are wrong" and status == 200


def test_add_song_to_db_successfully(clean_db):
    status, result = logic.addsong("Rap", "1999", "2Pac", "Dear Mama")
    data = result['data']
    message = result['message']
    assert data == "Dear Mama" and message == "OK" and status == 200


def test_add_existing_song_to_db(set_user_in_db):
    # song in db = "song_genre": "Rap", "song_performer": "2Pac", "song_title": "Dear Mama", "song_year": "1999"
    status, result = logic.addsong("Rap", "1999", "2Pac", "Dear Mama")
    message = result['error']
    assert message == "this song already exist in the collection" and status == 200


def test_add_song_to_playlist_successfully(set_user_playlist_and_song_in_db):
    # user in db = "user_name":"Linda", "user_password": "4321"
    # playlist in db = "user_name":"Linda", "user_password":"4321", "playlist_name":"Summer22")
    # song in db = "song_genre":"Rap", "song_year":"2003", "song_performer":"Eminem", "song_title":"Lose yourself"
    status, result = logic.addsongtoplaylist("Summer22", "Lose yourself", "Linda", "4321")
    data = result['data']
    message = result['message']
    assert data == "Lose yourself" and message == "OK", status == 200


def test_add_existing_song_to_play_list(set_user_and_song_in_playlist):
    # user in db = "user_name":"Linda", "user_password": "4321"
    # playlist in db = "user_name":"Linda", "user_password":"4321", "playlist_name":"Summer22")
    # song in db = "song_genre":"Rap", "song_year":"2003", "song_performer":"Eminem", "song_title":"Lose yourself"
    # song in user playlist in db = "playlist_name":"Summer22", "song_title":"Lose yourself", "user_name":"Linda","password":"4321"
    status, result = logic.addsongtoplaylist("Summer22", "Lose yourself", "Linda", "4321")
    message = result['error']
    assert message == "the song Lose yourself already exist in the playlist or not in the songs collection" and status == 200
