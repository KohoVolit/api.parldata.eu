======================
Installation and setup
======================

.. contents:: :backlinks: none

------------------------
Local development server
------------------------

The most convenient for development and testing of scrapers and applications is to install API on your computer and work locally. You don’t need to install and configure Apache webserver, a simple built-in application server comes with Eve REST API framework the Visegrad+ parliament API is built on.

Install `Python 3.3+`_, MongoDB_, git_, pip_, Eve_ and requests_ for your platform.

.. _`Python 3.3+`: https://www.python.org/download/
.. _MongoDB: http://docs.mongodb.org/manual/installation/
.. _git: http://git-scm.com/downloads
.. _pip: http://pip.readthedocs.org/en/latest/installing.html
.. _Eve: http://python-eve.org/install.html
.. _requests: http://docs.python-requests.org/en/latest/user/install/

Install the API:

.. code-block:: console

    $ git clone https://github.com/KohoVolit/visegrad-parliament-api.git

Start MongoDB server (on Ubuntu):

.. code-block:: console

    $ sudo service mongodb start        

or (on Windows):

.. code-block:: console

    $ net start mongodb

Run database shell and set-up a database for all your parliaments listed in ``/var/www/api.parldata.eu/parliaments.json`` file. Replace ``/`` characters with ``-`` in names of dbs. Example:

.. code-block:: console

    $ mongo
    > use xx-test
    > load('/var/www/api.parldata.eu/init_db.js')
    > quit()

Execute run.py (MongoDB server must be running every time you are executing run.py):

.. code-block:: console

    $ python3 run.py

Check http://127.0.0.1:5000 in your web-browser, the API should respond with list of resources.

`Postman Chrome extension`_ is very helpful to send API requests.

.. _`Postman Chrome extension`: http://www.getpostman.com

-----------------
Production server
-----------------

Assuming fresh Linux Ubuntu/Debian (Ubuntu 14.04 LTS) installed.

Install
=======

1. Apache (2.4) and its WSGI (3.4) module for Python 3

  .. code-block:: console

      $ sudo apt-get install apache2
      $ sudo apt-get install libapache2-mod-wsgi-py3

2. MongoDB (2.6)

  .. code-block:: console

      $ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
      $ echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
      $ sudo apt-get update
      $ sudo apt-get install mongodb-org

3. git (1.8)

  .. code-block:: console

      $ sudo apt-get install git

4. pip (1.5)

  .. code-block:: console

      $ cd /tmp
      $ sudo wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
      $ sudo python3 get-pip.py
      $ sudo rm get-pip.py

5. Eve

  .. code-block:: console

      $ sudo apt-get install build-essential python3-dev
      $ sudo pip install eve

6. VPAPI

  .. code-block:: console

      $ sudo pip install requests
      $ cd /var/www
      $ sudo git clone https://github.com/KohoVolit/visegrad-parliament-api.git
      $ sudo mv /var/www/visegrad-parliament-api /var/www/api.parldata.eu
      $ sudo mkdir /var/www/files.parldata.eu
      $ sudo chown :www-data /var/www/files.parldata.eu
      $ sudo chmod g+w /var/www/files.parldata.eu

Modify file ``/var/www/api.parldata.eu/parliaments.json`` to contain all available parliaments. Each record’s key is path to the parliament, field ``authorized_users`` specifies username(s) and password(s) of API users authorized to modify data of this parliament through API. (Read access is public.)

Setup MongoDB databases
=======================

Limit database connections to localhost only. Uncomment/add the following lines in file ``/etc/mongod.conf``

::

    bind_id = 127.0.0.1
    noauth = true
    nohttpinterface = true

and restart the database server

.. code-block:: console

    $ sudo service mongod restart

Run database shell and set-up a database for **each** parliament listed in ``/var/www/api.parldata.eu/parliaments.json`` file. Replace ``/`` characters with ``-`` in names of dbs. Example:

.. code-block:: console

    $ mongo
    > use xx-test
    > load('/var/www/api.parldata.eu/init_db.js')
    > quit()

Configure Apache (2.4)
======================

* Configure SSL

  Generate a self-signed certificate (fill in the following information when asked: *Country Name: EU, Organization Name: KohoVolit.eu, Common name: api.parldata.eu, Email address: admin\@parldata.eu* and leave the others blank (fill in .)):

  .. code-block:: console

     $ sudo mkdir /usr/local/apache2
     $ sudo openssl req -x509 -newkey rsa:2048 -keyout /etc/ssl/private/apache_key.pem -out /etc/ssl/certs/apache_cert.pem -days 3650 -nodes

  Enable Apache SSL support

  .. code-block:: console

      $ sudo a2enmod ssl

* Add the following line to ``/etc/apache2/apache2.conf``

  ::

      ServerName parldata.eu

* Make virtualhost **api.parldata.eu**

  Create file ``/etc/apache2/sites-available/api.parldata.eu.conf`` with content:

  ::

      <VirtualHost *:80>
          ServerName api.parldata.eu

          ErrorLog ${APACHE_LOG_DIR}/api.parldata.eu/error.log
          CustomLog ${APACHE_LOG_DIR}/api.parldata.eu/access.log combined

          <Directory /var/www/api.parldata.eu/>
              Require method GET HEAD OPTIONS
              AllowOverride None
              Order allow,deny
              Allow from all
          </Directory>

          WSGIDaemonProcess vpapi_80_process
          WSGIScriptAlias / /var/www/api.parldata.eu/wsgi.py
          WSGIProcessGroup vpapi_80_process
          WSGIApplicationGroup %{GLOBAL}
      </VirtualHost>

      <VirtualHost *:443>
          ServerName api.parldata.eu

          ErrorLog ${APACHE_LOG_DIR}/api.parldata.eu/error.log
          CustomLog ${APACHE_LOG_DIR}/api.parldata.eu/access.log combined

          <Directory /var/www/api.parldata.eu/>
              Require all granted
              AllowOverride None
              Order allow,deny
              Allow from all
          </Directory>

          WSGIDaemonProcess vpapi_443_process
          WSGIScriptAlias / /var/www/api.parldata.eu/wsgi.py
          WSGIProcessGroup vpapi_443_process
          WSGIApplicationGroup %{GLOBAL}
          WSGIPassAuthorization On

          SSLEngine on
          SSLCertificateFile /etc/ssl/certs/apache_cert.pem
          SSLCertificateKeyFile /etc/ssl/private/apache_key.pem
      </VirtualHost>

  Then

  .. code-block:: console

      $ sudo mkdir /var/log/apache2/api.parldata.eu
      $ sudo a2ensite api.parldata.eu

* Make virtualhost **files.parldata.eu**

  Create file ``/etc/apache2/sites-available/files.parldata.eu.conf`` with content:

  ::

      <VirtualHost *:80>
          ServerName files.parldata.eu
          DocumentRoot /var/www/files.parldata.eu

          ErrorLog ${APACHE_LOG_DIR}/files.parldata.eu/error.log
          CustomLog ${APACHE_LOG_DIR}/files.parldata.eu/access.log combined

          <Directory /var/www/files.parldata.eu/>
              Require all granted
              Options FollowSymlinks
              AllowOverride None
              Order allow,deny
              Allow from all
          </Directory>
      </VirtualHost>

  Then

 .. code-block:: console

      $ sudo mkdir /var/log/apache2/files.parldata.eu
      $ sudo a2ensite files.parldata.eu

* Add the following line to ``/etc/apache2/envvars``

  ::

      export EVE_SETTINGS=/var/www/api.parldata.eu/settings_production.py

* Reload Apache configuration

 .. code-block:: console

      $ sudo service apache2 reload

--------------------------
Adding of a new parliament
--------------------------

Add a new record into ``/var/www/api.parldata.eu/parliaments.json``, e.g.

    ::

        "sk/nrsr": {
             "authorized_users": [
                 ["scraper", "secret"]
             ]
        }

with path to the parliament as a key and username(s) and password(s) of API users authorized to modify data of this parliament through API. (Read access is public.) Don’t forget to add comma behind the previous record to have a valid JSON document.

Run database shell and set-up a database for the new parliament. Replace ``/`` characters with ``-`` in name of the db. E.g.

 .. code-block:: console

    $ mongo
    > use sk-nrsr
    > load('/var/www/api.parldata.eu/init_db.js')
    > quit()

And reload Apache configuration

 .. code-block:: console

    $ sudo service apache2 reload

-----------------
Testing on remote
-----------------

It is recommended to install API on your computer to develop and test scrapers and applications completely locally.

However, if you prefer not do so and work over the network, add a test parliament (e.g. ``sk/nrsr-test``) on production server and use it during development and testing. Remember that path to the parliament must be in  form of ``<country-code>/<parliament-code>`` and none of the codes can contain the / character. (The MongoDB database name to create in this example would be ``sk-nrsr-test``.)
