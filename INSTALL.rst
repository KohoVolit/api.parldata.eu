======================
Installation and setup
======================

.. contents:: :backlinks: none

------------------------
Local development server
------------------------

The most convenient for development and testing of scrapers and applications is to install API on your computer and work locally. You don’t need to install and configure Apache webserver, a simple built-in application server comes with Eve REST API framework the Visegrad+ parliament API is built on.

Install `Python 3.3+`_, MongoDB_ or TokuMX_, git_, pip_, Eve_, requests_ and pytz_ for your platform.

.. _`Python 3.3+`: https://www.python.org/download/
.. _MongoDB: http://docs.mongodb.org/manual/installation/
.. _TokuMX: http://docs.tokutek.com/tokumx/tokumx-installation.html
.. _git: http://git-scm.com/downloads
.. _pip: http://pip.readthedocs.org/en/latest/installing.html
.. _Eve: http://python-eve.org/install.html
.. _requests: http://docs.python-requests.org/en/latest/user/install/
.. _pytz: http://pythonhosted.org/pytz/

Install the API:

.. code-block:: console

    $ sudo git clone https://github.com/KohoVolit/api.parldata.eu.git api

Start MongoDB server or TokuMX server (example for Ubuntu):

.. code-block:: console

    $ sudo service mongod start

Run database shell (``mongo`` or ``tokumx``) and set-up a database for each of your parliaments listed in ``conf/parliaments.json`` file. Replace ``/`` and ``-`` characters with ``_`` in names of dbs. Example:

.. code-block:: console

    $ mongo
    > use xx_example
    > load('js/init_db.js')
    > quit()

Execute run.py (database server must be running every time you are executing run.py):

.. code-block:: console

    $ python3 run.py

Check http://127.0.0.1:5000 in your web-browser, the API should respond with list of resources.

`Postman Chrome extension`_ is very helpful to send API requests.

.. _`Postman Chrome extension`: http://www.getpostman.com

-----------------
Production server
-----------------

Assuming fresh Linux Ubuntu/Debian (Ubuntu 14.04 LTS) installed.

Set server timezone to UTC

  .. code-block:: console

      $ sudo timedatectl set-timezone UTC

Install
=======

1. Apache (2.4) and its WSGI (4.3) module for Python 3

  .. code-block:: console

      $ sudo apt-get install apache2 libapache2-mod-wsgi-py3

  **A temporary fix:** mod_wsgi 4.2+ `is needed`_ for Python 3.4. If there is
  no such package yet for the used Linux distribution, install from sources:

  .. _`is needed`: https://code.djangoproject.com/ticket/22948

  .. code-block:: console

      $ sudo apt-get install apache2-mpm-event apache2-dev
      $ cd /tmp
      $ wget https://github.com/GrahamDumpleton/mod_wsgi/archive/4.3.0.tar.gz
      $ tar xvfz 4.3.0.tar.gz
      $ cd mod_wsgi-4.3.0
      $ ./configure --with-python=/usr/bin/python3
      $ make
      $ sudo make install
      $ cd ..
      $ rm -r 4.3.0.tar.gz mod_wsgi-4.3.0
      $ sudo apt-get purge apache2-mpm-event apache2-dev
      $ sudo apt-get autoremove

2. MongoDB (2.6)

  .. code-block:: console

      $ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
      $ echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
      $ sudo apt-get update
      $ sudo apt-get install mongodb-org

  or TokuMX (2.0)

  .. code-block:: console

      $ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key 505A7412
      $ echo "deb [arch=amd64] http://s3.amazonaws.com/tokumx-debs $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/tokumx.list
      $ sudo apt-get update
      $ sudo apt-get install tokumx
      $ sudo update-rc.d tokumx defaults

3. git (1.8)

  .. code-block:: console

      $ sudo apt-get install git

4. pip (1.5)

  .. code-block:: console

      $ cd /tmp
      $ wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
      $ sudo python3 get-pip.py
      $ rm get-pip.py
      $ sudo apt-get install build-essential python3-dev

5. virtualenv (1.11) and create and activate a virtual environment for the API

  .. code-block:: console

      $ sudo pip install virtualenv
      $ sudo mkdir -p /home/projects/.virtualenvs
      $ sudo virtualenv /home/projects/.virtualenvs/api --no-site-packages
      $ source /home/projects/.virtualenvs/api/bin/activate

6. Visegrad+ parliament API

  .. code-block:: console

      (api)$ cd /home/projects
      (api)$ sudo git clone https://github.com/KohoVolit/api.parldata.eu.git api
      (api)$ sudo pip install -r api/requirements.txt
      (api)$ deactivate
      $ sudo cp api/conf/countries-example.json api/conf/countries.json
      $ sudo cp api/conf/parliaments-example.json api/conf/parliaments.json
      $ sudo mkdir /var/www/files.parldata.eu
      $ sudo chown :www-data /var/www/files.parldata.eu
      $ sudo chmod g+w /var/www/files.parldata.eu


Setup MongoDB or TokuMX databases
=================================

Limit database connections to localhost only. Uncomment/add the following lines in file ``/etc/mongod.conf`` or ``/etc/tokumx.conf``

::

    bind_ip = 127.0.0.1
    noauth = true
    nohttpinterface = true

and restart the database server

.. code-block:: console

    $ sudo service mongod restart

Configure Apache (2.4)
======================

* Configure SSL

  Generate a self-signed certificate (fill in the following information when asked: *Country Name: EU, Organization Name: KohoVolit.eu, Common name: api.parldata.eu, Email address: info\@kohovolit.eu* and leave the others blank (fill in .)). You may need to adjust the ``openssl.cnf`` file before to have *subjectAltName* in the certificate and prevent security warnings later when using it. See this `how-to`_.

  .. _`how-to`: https://stackoverflow.com/questions/21488845/how-can-i-generate-a-self-signed-certificate-with-subjectaltname-using-openssl

  .. code-block:: console

     $ sudo openssl req -x509 -newkey rsa:2048 -keyout /etc/ssl/private/apache_key.pem -out /etc/ssl/certs/apache_cert.pem -days 3650 -nodes

  Enable Apache SSL support

  .. code-block:: console

      $ sudo a2enmod ssl

* Add the following line to ``/etc/apache2/apache2.conf``

  ::

      ServerName parldata.eu

* Make virtualhosts **api.parldata.eu** and **files.parldata.eu**

  .. code-block:: console

      $ sudo cp /home/projects/api/api.parldata.eu.conf /etc/apache2/sites-available/
      $ sudo mkdir /var/log/apache2/api.parldata.eu
      $ sudo a2ensite api.parldata.eu
      $ sudo cp /home/projects/api/files.parldata.eu.conf /etc/apache2/sites-available/
      $ sudo mkdir /var/log/apache2/files.parldata.eu
      $ sudo a2ensite files.parldata.eu

* Add the following lines to ``/etc/apache2/envvars``

  ::

      sudo export EVE_SETTINGS=/home/projects/api/settings_production.py
      sudo export LANG='en_US.UTF-8'
      sudo export LC_ALL='en_US.UTF-8'

* Reload Apache configuration

  .. code-block:: console

      $ sudo service apache2 reload

--------------------------
Adding of a new parliament
--------------------------

Add a new record to the list within the respective country code key in ``/home/projects/api/conf/parliaments.json``, e.g.

.. code-block:: json

    "sk": [
        {
            "name": "Národná rada Slovenskej republiky",
            "code": "nrsr",
            "authorized_users": [
                ["scraper", "secret"]
            ]
        }
    ]

Username(s) and password(s) of API user(s) authorized to modify data of this parliament through API is specified in ``authorized_users`` list. (Read access is public.) Don’t forget to add comma behind the previous record to have a valid JSON document. When introducing a new country add also its record into ``/home/projects/api/conf/countries.json``.

Run database shell (``mongo``) and set-up a database for the new parliament. Replace ``/`` and ``-`` characters with ``_`` in name of the db. E.g.

.. code-block:: console

    $ mongo
    > use sk_nrsr
    > load('/home/projects/api/js/init_db.js')
    > quit()

And reload Apache configuration

.. code-block:: console

    $ sudo service apache2 reload

-----------------
Testing on remote
-----------------

It is recommended to install API on your computer to develop and test scrapers and applications completely locally.

However, if you prefer not do so and work over the network, add a test parliament (e.g. ``sk/nrsr-test``) on production server and use it during development and testing. Remember that path to the parliament must be in  form of ``<country-code>/<parliament-code>`` and none of the codes can contain the / character. (The MongoDB database name to create in this example would be ``sk_nrsr_test``.)
