import requests
import json
import InfrastructureLayer.RestManagment as REST


def getuser(username):
    response = REST.GetFromServer("/users/get_user", "?user_name=" + username)
    # return user['data']['user_name']
    return response.status_code,response.json()


def adduser(user):
    response = REST.PostOnServer("/users/add_user", user)
    return response.status_code, response.json()
    # return response['data'], response['message']


def addfriend(username, password, friendname):
    data = {
        "user_name": username,
        "user_password": password,
        "friend_name": friendname
    }
    response = REST.PutOnServer("/users/add_friend", data).json()
    return response.status_code, response.json()
    # return response['data'], response['message']


def addplaylist(username, password, playistName):
    data = {
        "user_name": username,
        "user_password": password,
        "playlist_name": playistName
    }
    response = REST.PostOnServer("/users/add_playlist", data)
    return response.status_code, response.json()
    # return response['data'], response['message']


def addsong(genre, year, performer, title):
    song = {
        "song_genre": genre,
        "song_performer": performer,
        "song_title": title,
        "song_year": year
    }
    response = REST.PostOnServer("/songs/add_song", song)
    return response.status_code, response.json()
    # return response['data'], response['message']


def getsong(songtitle):
    title = songtitle.replace(" ", "%20")
    response = REST.GetFromServer("/songs/get_song", "?song_title=" + title)
    return response.status_code, response.json()


def upvotesong(playlistname, songtitle, username, password):
    votedata = {
        "playlist_name": playlistname,
        "song_title": songtitle,
        "user_name": username,
        "user_password": password
    }
    response = REST.PutOnServer("/songs/upvote", votedata)
    return response.status_code, response.json()


def downvotesong(playlistname, songtitle, username, password):
    votedata = {
        "playlist_name": playlistname,
        "song_title": songtitle,
        "user_name": username,
        "user_password": password
    }
    response = REST.PutOnServer("/songs/upvote", votedata)
    return response.status_code, response.json()


def addsongtoplaylist(playlistname, songtitle, username, userpassword):
    data = {
        "playlist_name": playlistname,
        "song_title": songtitle,
        "user_name": username,
        "user_password": userpassword
    }
    response = REST.PostOnServer("/playlists/add_song", data)
    return response.status_code, response.json()


def getplaylist(username, password, playlistname):
    response = REST.GetFromServer("/users/get_playlist",
                                 "?user_name=" + username + "&user_password=" + password + "&playlist_name=" + playlistname)
    return response.status_code, response.json()


def getsongbyrank(rank, op):
    response = REST.GetFromServer("/songs/ranked_songs", "?rank=" + rank + "&op=" + op)
    return response.status_code, response.json()


def changeuserpassword(username, newpassword, oldpassword):
    data = {
        "user_name": username,
        "user_new_password": newpassword,
        "user_password": oldpassword
    }
    response = REST.PutOnServer("/users/change_password", data)
    return response.status_code, response.json()


# =========admin methods for testing=============

def deleteallusers():
    response = REST.delete_From_Server("/admin/delete_all_users", "").json()
    return


def deleteallsongs():
    response = REST.delete_From_Server("/admin/delete_all_songs", "").json()
    return