from setup_app.config.config import Config


class APPConfig():
    host = Config().get_config(key="mysql_host")
    username = Config.get_config(key="mysql_username")
    password = Config.get_config(key="mysql_password")
    db_name = Config.get_config(key="mysql_db_name")

    DEBUG = True
    TESTING = True
    SESSION_COOKIE_NAME = 'vasid'
    SECRET_KEY = 'trY t0 Hit iT'
    SQLALCHEMY_DATABASE_URI = 'mysql://' + username + ':' + password + '@' + host + '/' + db_name
    SQLALCHEMY_TRACK_MODIFICATIONS = False
