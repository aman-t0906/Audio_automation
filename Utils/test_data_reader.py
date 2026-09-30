import json


def load_audio_test_data():
    with open("test_data/audio_tests.json","r") as file:
        data = json.load(file)
        return data["audio_tests"]