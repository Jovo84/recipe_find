import importlib

from env import env

class Config(object):

    @staticmethod
    def get_config(key, default_value=None):
        config_module = importlib.import_module('recipe_app.config.' + env)
        return config_module.config[key] if key in config_module.config else default_value
