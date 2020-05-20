# 环境搭建
### 一、安装包
>pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django==2.1
>

### 二、项目初始化
django-admin startproject Blog

cd Blog

运行项目  
python manage.py runserver

创建一个项目
python manage.py startapp article

修改了模型之后，我们需要将应用迁移到数据库中，模型的更改同步到数据库结构  
python manage.py makemigrations
python manage.py migrate

每当你修改了models.py文件，都需要用makemigrations和migrate这两条指令迁移数据。
在迁移之后，Model的编写就算完成了。


网站后台，创建管理员账号  
python manage.py createsuperuser

https://www.dusaiphoto.com/article/detail/18/

安装 md
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple markdown

代码高亮  
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple Pygments

编写用户模块
python manage.py startapp userprofile

安装重置密码模块
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -U django-password-reset

更新视图，要进行数据库迁移
python manage.py makemigrations
python manage.py migrate

创建评论功能  
python manage.py startapp comment

https://www.dusaiphoto.com/article/detail/50/cd

