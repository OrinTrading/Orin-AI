import json

class DataHandler:
    @staticmethod
    def load_user_profiles(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def save_user_profiles(file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

