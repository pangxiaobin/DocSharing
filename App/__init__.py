#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 19-10-21 下午3:00
# @Author  : Hubery
# @File    : __init__.py
# @Software: PyCharm

from flask import Flask

from App.ext import init_ext
from App.settings import envs, TEMPLATES_FOLDER, STATIC_FOLDER
from App.views import init_blue


def create_app():
    app = Flask(__name__, template_folder=TEMPLATES_FOLDER, static_folder=STATIC_FOLDER)
    app.config.from_object(envs.get('develop'))
    init_blue(app)
    init_ext(app)
    return app