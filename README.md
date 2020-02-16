## 功能简介：

- 商品浏览：商品的图片，售价，种类，简介以及库存等信息。
- 全文检索：支持对商品种类以及商品名称，简介的检索。
- 登录注册：用户的登录与注册。
- 用户中心：支持用户个人信息，收货地址等信息的更新，商品加入购物车，订单生成。
- 商品下单：在支付接口和企业资质的支持下可完成商品的下单功能，按照原子事务处理，下单异常则终止此次下单过程。
- 后台管理：支持后台管理功能，商品及用户信息的增加，更新与删除，可自定制样式与功能，日志，以及权限的管理和分配。

### 环境
- Python 3.7
- MySQL 8.0

### 依赖包安装

下载文件进入项目目录之后，使用pip安装依赖包

<code>pip install -r requirements.txt</code>

### 数据库配置
#### 以下所有命令都是在项目根目录执行
#### 如果使用windows，并且项目在D:\毕设\daily_fresh_demo保存
#### 使用以下命令切换到项目根目录

    D:
    cd D:\毕设\daily_fresh_demo
    
进入mysql命令行, 创建数据库（假设你用户名为root，密码为123456)
    
    $ mysql -uroot -p123456
    mysql> create database daily_fresh;

修改daily_fresh_deme/settings.py中的DATABASE(假设你用户名为root，密码为root)

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'daily_fresh',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    },

创建表

    python manage.py migrate
    
插入测试数据(注意插入顺序不能颠倒)
    
    $ mysql -uroot -p
    mysql> use daily_fresh;
    mysql> source sql/df_goods_typeinfo.sql;
    mysql> source sql/df_goods_goodsinfo.sql;
    
### 创建超级用户

终端下执行:

    python manage.py createsuperuser

然后输入相应的超级用户名以及密码，邮箱即可。

### 开始运行

终端下执行:

    python manage.py runserver

浏览器打开: <code>http://127.0.0.1</code> 即可进入普通用户入口

浏览器打开: <code>http://127.0.0.1/admin</code> 即可进入超级用户入口
