#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 19-10-21 下午2:30
# @Author  : Hubery
# @File    : manage.py
# @Software: PyCharm

from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app

app = create_app()

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
