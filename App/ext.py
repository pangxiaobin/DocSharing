#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 19-10-21 下午3:00
# @Author  : Hubery
# @File    : ext.py
# @Software: PyCharm

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # 数据库api接口
migrate = Migrate()  # 数据迁移


def init_ext(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)