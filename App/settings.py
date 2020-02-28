#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 19-10-21 下午3:04
# @Author  : Hubery
# @File    : settings.py
# @Software: PyCharm

import os

BASE_DIR = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))

TEMPLATES_FOLDER = os.path.join(BASE_DIR, 'templates')
STATIC_FOLDER = os.path.join(BASE_DIR, 'static')


def get_db_uri(db_info):

    ENGINE = db_info.get('ENGINE') or 'mysql'
    DRIVER = db_info.get('DRIVER') or 'pymysql'
    USER = db_info.get('USER') or 'root'
    PASSWORD = db_info.get("PASSWORD") or 'root'
    HOST = db_info.get('HOST') or 'localhost'
    PORT = db_info.get('PORT') or '3306'
    NAME = db_info.get('NAME') or 'test'
    return '{}+{}://{}:{}@{}:{}/{}'.format(ENGINE, DRIVER, USER, PASSWORD, HOST, PORT, NAME)


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'docsharing'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class TestingConfig(Config):
    DEBUG = True

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'docsharing'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class StagingConfig(Config):
    DEBUG = True

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'docsharing'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ProductConfig(Config):
    DEBUG = False

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'docsharing'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

envs = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
    'default': DevelopConfig
}