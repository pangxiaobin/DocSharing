#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 19-10-21 下午3:13
# @Author  : Hubery
# @File    : views.py
# @Software: PyCharm
from flask import request, jsonify, redirect
from flask import Blueprint, render_template

from App.ext import db
from App.helper import gen_url
from App.models import Project, FolderName, FileName

bule = Blueprint('main', __name__)


def init_blue(app):
    app.register_blueprint(blueprint=bule)


@bule.route('/')
def index():
    projects = Project.query.all()
    return render_template('home.html', projects=projects)


@bule.route('/create_project/', methods=['POST'])
def create_project():
    """创建项目"""
    data = request.form
    name = data.get('name')
    # email = data.get('email')
    # password = data.get('password')
    url = gen_url()
    # project = project(name=name, email=email, password=password, url=url)
    project = Project(name=name, url=url)
    db.session.add(project)
    db.session.commit()
    return redirect('/project/{}/'.format(project.url))


@bule.route('/project/', methods=['POST', 'GET'])
@bule.route('/project/<url>/')
def get_project(url=None):
    """获取项目内容"""
    if request.method == "POST":
        project_name = request.form.get('name')
        # password = request.form.get('password')
        project = Project.query.filter_by(name=project_name).first()
        if project:
            return jsonify({'url': project.url, 'code': '200', 'message': 'success'})
        return jsonify({'code': '404', 'message': 'not found'})
    else:
        project = Project.query.filter_by(url=url).first()
        if project:
            return render_template('project.html', project=project)
        return render_template('404.html')


@bule.route('/check_project/')
def check_project():
    """检查房间名是否已存在"""
    name = request.args.get('name')
    project = Project.query.filter(Project.name == name).count()
    if project > 0:
        return {'msg': 'Data already exists', 'status': '900'}
    return {'msg': 'Ok', 'status': '200'}


@bule.route('/folder_files/')
def get_folder_files():
    """获取房间内包含的文件夹和文件"""
    project_id = request.args.get('project_id')
    folders = FolderName.query.filter_by(project_id=project_id)
    data = []
    for folder in folders:
        tem_dict1 = dict()
        folder_id = folder.id
        tem_dict1['id'] = folder_id
        title = folder.name
        tem_dict1['title'] = title if title.__len__() < 14 else '{}...'.format(title[:14])
        tem_dict1['parentId'] = '0'
        tem_dict1['last'] = False
        files = folder.files.all()
        tem_dict1['children'] = [
            {'id': file.id, 'title': file.name if file.name.__len__() < 11 else '{}...'.format(file.name[:10]),
             'parentId': folder_id, 'last': True, 'basicData': file.file_type} for
            file in
            files]
        data.append(tem_dict1)
    result = {
        "status": {"code": 200, "message": "操作成功"},
        'data': data
    }
    return jsonify(result)


@bule.route('/create_folder/', methods=['POST'])
def create_folder():
    data = request.form
    folder_name = data.get('folder_name', '')
    project_id = data.get('project_id', '')
    folder = FolderName(name=folder_name, project_id=project_id)
    db.session.add(folder)
    db.session.commit()
    return jsonify({'code': '200', 'message:': 'success'})


@bule.route('/update_folder_file/', methods=['POST'])
def update_folder_file():
    """重命名"""
    data = request.form
    leaf = data.get('leaf')
    node_id = data.get('nodeId')
    new_name = data.get('editNodeName')
    if leaf == 'false':
        edit_ = FolderName.query.get(node_id)
    else:
        edit_ = FileName.query.get(node_id)

    if not edit_:
        return jsonify({'code': '404'})
    edit_.name = new_name
    db.session.commit()
    return jsonify({'code': '201', 'msesage': 'change success'})


@bule.route('/create_file/', methods=['POST'])
def create_file():
    data = request.form
    folder_id = data.get('parentId')
    name = data.get('context')
    file_type = data.get('file_type')
    file = FileName(name=name, file_type=file_type, folder_id=folder_id)
    db.session.add(file)
    db.session.flush()
    db.session.commit()
    return jsonify({"code": 200, "message": "success", "nodeId": file.id, "name": name, "fileType": file_type})


@bule.route('/update_file/', methods=['POST'])
def update_file():
    """更新"""
    data = request.form
    file_id = data.get('file_id', None)
    content = data.get('content', None)
    file = FileName.query.get(file_id)
    if not file:
        return jsonify({'code': '404'})
    file.content = content
    db.session.commit()
    return jsonify({'code': '201', 'message:': 'success change'})


@bule.route('/get_file/', methods=['GET'])
def get_file():
    """
    获取文件内容
    :return:
    """
    file_id = request.args.get('file_id')
    file = FileName.query.get(file_id)
    if file:
        return jsonify({'code': '200', 'message': 'success', 'content': file.content, 'type': file.file_type})
    return jsonify({'code': '404', 'message': 'not fond'})


@bule.route('/show_project/<url>/', methods=['GET'])
def show_project(url=None):
    project = Project.query.filter_by(url=url).first()
    if project:
        folders = FolderName.query.filter_by(project_id=project.id)
        return render_template('show_project.html', folders=folders)
    else:
        return render_template('404.html')


@bule.route('/file_detail/', methods=['GET'])
def file_detail():
    file_id = request.args.get('file_id')
    file = FileName.query.get(file_id)
    return jsonify({'code':'200', 'content': file.content, 'type': file.file_type})