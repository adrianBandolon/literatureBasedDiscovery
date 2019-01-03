from Calculations.DocumentFilepaths import fish_oil_filepath, raynauds_filepath
import os


def create_dict_from_function(function):
    dict_to_return = {}
    for directory in [fish_oil_filepath, raynauds_filepath]:
        for file_name in os.listdir(directory):
            key, value = function(directory, file_name)
            dict_to_return[key] = value
    return dict_to_return
