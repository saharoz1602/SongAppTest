import requests
import json

from InfrastructureLayer import config_reader


def GetFromServer(path, message):
    try:
        r = requests.get(url='http://' + config_reader.host + config_reader.port + path + message)
        return r
    except requests.exceptions.RequestException as e:
        print(e)


def delete_From_Server(path, message):
    try:
        # r = requests.delete(url=path, json=message)
        r = requests.request("DELETE", url='http://' + config_reader.host + config_reader.port + path, json=message)
        return r
    except requests.exceptions.RequestException as e:
        print(e)


def PutOnServer(path, message):
    try:
        r = requests.put(url='http://' + config_reader.host + config_reader.port + path, json=message)
        return r
    except requests.exceptions.RequestException as e:
        print(e)


def PostOnServer(path, message):
    try:
        r = requests.request("POST", url='http://' + config_reader.host + config_reader.port + path, json=message)
        return r
    except requests.exceptions.RequestException as e:
        print(e)


song = {
    "song_genre": "Rap",
    "song_performer": "2Pac",
    "song_title": "Dear mama",
    "song_year": "1999"
}


#print(PutOnServer("/users/add_friend",z).json())

#print(PostOnServer("/songs/add_song",song).json())
