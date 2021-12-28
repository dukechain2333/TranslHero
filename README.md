# TranslHero

A tool to help you translate multiple languages. (Web-based translation application using Baidu Translation api).

![](https://img.shields.io/badge/dependencies-Python%203.8--3.9-blue)
![](https://img.shields.io/badge/dependencies-Django%204.0-green)
![](https://img.shields.io/badge/tests-Chrome%2089--92%20%E2%9C%94-brightgreen)

## Install

1. Get your Django secret key from  [Djecrety](https://djecrety.ir/) and fill it in `django_secret_key`
2. Set `ALLOWED_HOSTS` option
3. Fill in the `APPID` and `APPKEY` option. You may get this information at [Baidu Fanyi](https://api.fanyi.baidu.com/)
4. Use `pip install -r requirements.txt` to install dependencies.
5. Put following command into your command prompt

```bash
python manage.py collectstatic
```

5. Enter the following command into your command prompt to initialize the database.

```bash
python manage.py makemigrations
python manage.py migrate
```

6. The following command will help you to create a superuser.

```bash
python manage.py createsuperuser
```

7. Use the following command to start the Django service

```bash
python manage.py runserver
```

- Usually, the service will automatically run on `port:8000`.  
  And you should notice that the host and port can be modified by running those commands

```bash
python manage.py runserver <your_host>:<your_port>
```

- You may get more details by visiting [Django Documents](https://www.djangoproject.com/)

## Usage

1. By visiting `http://<your_host>:<your_port>/`, you are good to go.

## Licence

MIT License

Copyright (C) 2021 ZHChain