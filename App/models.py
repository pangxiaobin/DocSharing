#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 19-10-21 下午3:17
# @Author  : Hubery
# @File    : models.py
# @Software: PyCharm
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash  # 转换密码用到的库

from App.ext import db


class Project(db.Model):
    """房间"""
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(32), nullable=False)
    name = db.Column(db.String(256), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=True)
    password_hash = db.Column(db.String(256), nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    folders = db.relationship('FolderName', backref='project', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError("密码不允许读取")

    # 转换密码为hash存入数据库
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 检查密码
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class FolderName(db.Model):
    """文件夹名"""
    __tablename__ = 'folder_names'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    files = db.relationship('FileName', backref='folder', lazy='dynamic')


class FileName(db.Model):
    """文件名"""
    __tablename__ = 'file_names'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=True)
    content = db.Column(db.Text, nullable=True)
    file_type = db.Column(db.Integer, nullable=True, default=1)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    folder_id = db.Column(db.Integer, db.ForeignKey('folder_names.id'))
