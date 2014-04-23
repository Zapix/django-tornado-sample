django-tornado-sample
=====================

Simple django application with tornado for websocket

Setup application
-----------------

Configure ubuntu with required libs

```sh
    $ sudo apt-get install -y python-pip
    $ sudo apt-get install -y python-dev
    $ sudo apt-get install -y libzmq-dev
```

Setup virtual env & install requirements.txt

```sh
    $ mkvirtualenv testapp
    $ pip install -r requirements.txt
```

Start application
-----------------

Syncdb:

```sh
    $ cd djangotornadosample
    $ ./manage.py syncdb
```

Start web server

```sh
    $ ./manage.py runserver 0.0.0.0:8000
```

Setup site domain name on django admin panel.

Start generator on console

```sh
    $ ./manage.py genrandom
```

Start tornado server on another tab

```sh
   $ ./manage.py runtornado
```
