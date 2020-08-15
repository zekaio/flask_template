# -*- coding: utf-8 -*-
class BaseConfig:
    pass


DatabaseConfig = dict(
    username='',
    password='',
    host='localhost',
    port=3306
)

dbname = {
    'development': '',
    'production': '',
    'testing': ''
}

baseurl = 'mysql+mysqlconnector://{username}:{password}@{host}:{port}'.format(**DatabaseConfig)


class AppConfig:
    SECRET_KEY = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORD_QUERIES = True
    DEBUG = False


class AppConfigDev(AppConfig):
    SQLALCHEMY_DATABASE_URI = baseurl + '/{}?charset=utf8mb4'.format(dbname['development'])
    DEBUG = True


class AppConfigProd(AppConfig):
    SQLALCHEMY_DATABASE_URI = baseurl + '/{}?charset=utf8mb4'.format(dbname['production'])
    SQLALCHEMY_RECORD_QUERIES = False


class AppConfigTest(AppConfig):
    SQLALCHEMY_DATABASE_URI = baseurl + '/{}?charset=utf8mb4'.format(dbname['testing'])
    TESTING = True


app_config = {
    'development': AppConfigDev,
    'production': AppConfigProd,
    'testing': AppConfigTest
}
