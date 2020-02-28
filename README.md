## 文档分享
### 项目介绍
- 后端基于[flask](https://github.com/pallets/flask)框架开发
- 前端ui使用[layui](https://www.layui.com/doc/element/color.html)
- 树形结构使用[dtree](http://www.wisdomelon.com/DTreeHelper/)
- 富文本使用[wangEditor](https://github.com/wangfupeng1988/wangEditor)
- markdown插件使用[tui-editor](https://github.com/nhn/tui.editor)
### 快速开始
 - 下载 
 ```shell
git clone https://github.com/pangxiaobin/DocSharing.git 
cd DocSharing
``` 
- 安装依赖
```shell
# 创建虚拟环境  需要安装virtualenv 和virtualenvwrapper
mkvirtualenv doc
pip install -r requments.txt
# 注释 windows pip install uwsgi 会报错 windows下演示可先在requments.txt 注释掉uwsgi
```
- 本地测试
    - 配置数据库
    ```sql
    # 连接数据库
     mysql -uroot -p
    # 创建数据库
     create database docshaing charset=utf8;
    ```
    - 修改配置文件
    ```
      # DocSharing/App/setting.py
      # 修改PASSWORD
      DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'docsharing'
    }
    ```
   - 进行数据表映射
   ```shell
   # 初始化
   python manage.py db init
   # 生成迁移文件
   python manage.py db migrate 
   # 执行迁移
   python manage.py db upgrade
   ```
   - 运行项目
   ```shell
   python manage.py runserver
   ```
- 项目服务器部署
   - 参考文章[flask+uwsgi+nginx](https://juejin.im/post/5ccd3695f265da03587c0d9d)
   
### 效果图

 ![首页](https://github.com/pangxiaobin/DocSharing/blob/master/images/home.png) 
 ![项目列表页](https://github.com/pangxiaobin/DocSharing/blob/master/images/project_list.png) 
 ![项目编辑页](https://github.com/pangxiaobin/DocSharing/blob/master/images/project_edit.png) 
 ![项目详情展示页](https://github.com/pangxiaobin/DocSharing/blob/master/images/project_show.png) 
   