=====================
Full read-write usage
=====================

.. contents:: :backlinks: none

The API provides means to create, read, update and delete the data. Read access is public (see README_), while modification of the data needs authentication. Operations are implemented by HTTP methods following REST_ best practices.

.. _README: README.rst
.. _REST: http://en.wikipedia.org/wiki/Representational_state_transfer#Applied_to_web_services

-------
Methods
-------

+-----------+------------------------------------------+-----------------------------------+
|HTTP method|on data collection                        |on item                            |
+===========+==========================================+===================================+
|GET        |read all items satisfying given parameters|read the item                      |
+-----------+------------------------------------------+-----------------------------------+
|POST       |create item(s)                            |N/A                                |
+-----------+------------------------------------------+-----------------------------------+
|PUT        |N/A                                       |replace the whole item by a new one|
+-----------+------------------------------------------+-----------------------------------+
|PATCH      |N/A                                       |update given properties of the item|
+-----------+------------------------------------------+-----------------------------------+
|DELETE     |delete all items                          |delete the item                    |
+-----------+------------------------------------------+-----------------------------------+

--------------
Authentication
--------------

Requests that modify the data (all methods except GET) require the user to authenticate. `Basic authentication`_ is used secured by HTTPS protocol.

.. _`Basic authentication`: http://en.wikipedia.org/wiki/Basic_authentication

Basic authentication requires the client to send an *Authorization* HTTP header with content constructed as follows: A string "username:password" (without quotes and with actual username and password) is encoded by Base64 and string "Basic " is prepended. See `Basic authentication`_ at Wikipedia.

Use ``https://...`` and the above header for all data modifying requests.

-------------------
Time and time zones
-------------------

All datetime values are assumed to be in UTC time, ISO 8601 format without time zone is used (example: 2014-05-17T12:34:56). You can use helper functions `timezone`, `local_to_utc` and `utc_to_local` of the `Client module`_ to convert between local time and UTC time on the client side.

-----------------
Specific features
-----------------

Bulk inserts
============

Any number of items of a resource can be created by one POST request. Just send a JSON list of items instead of one item in request body. This way is much more efficient for large amounts of data. See `Bulk inserts`_ in Eve documentation for an example.

.. _`Bulk inserts`: http://python-eve.org/features.html#bulk-inserts

Validation
==========

All data are validated against Popolo_ schemas on creation or modification of items. In case that validation of at least one item fails, the result is *4xx* HTTP response. Result of validation for each inserted/modified item can be found in the ``_status`` field of the response. See `Data validation`_ in Eve documentation for an example.

.. _Popolo: http://popoloproject.com
.. _`Data validation`: http://python-eve.org/features.html#data-validation

Automatic tracking of changes
=============================

The API automatically tracks history of all properties that are expected to change value at least occasionally. If property value changes, the former value is automatically stored to the ``changes`` property that collects all changes within the item. A period of validity is stored together with the former value.

The history we want to track is the *actual history* with periods when the former values were valid in the real world. Not the *change history* when the value was changed in our database. Nevertheless, in daily updated data both dates coincide – if a change was detected in source data today, it is assumed the value actually changed today. There is no other source to get the date of actual change from.

Because of the above, when a change takes place, the time period of the former value is set until yesterday by default. In case you want to simulate data update effective to a different date than today, set an explicit date in URL parameters by ``effective_date=YYYY-MM-DD``.

If you need to *correct* an error in the data rather than *update*, the change should not be logged to ``changes``. Use ``effective_date=fix`` in that case and the change will not be logged.

For a reference of all properties with tracked history look for ``track_changes`` in the ``schemas/`` directory.

Mirroring of referenced files
=============================

Some of the files or documents referenced in properties (``person.image``, ``organization.image``) are mirrored and URL in the corresponding property is adjusted to point the local copy. Thus all the data are available even when the source website is offline, also older versions of the file are kept when the content changes.

Document embedding
==================

`Embedding of referenced items`_ is a convenient way to get all related data in one request. It works only when reading the data. You cannot send a document with embedded related items to create them automatically. Instead, they must be created first and their id-s provided to the referencing item on its creation.

.. _`Embedding of referenced items`: README.rst#embed

-------------
Client module
-------------

There is a `client module for Python`_ that constructs the HTTP requests for you and supports full access to the API and authentication.

.. _`client module for Python`: README.rst#client-module

Example of usage:

.. code-block:: Python

    import vpapi
    vpapi.parliament('xx/example')
    vpapi.authorize('user', 'password')

    mps = [
        {'name': 'Martin Fedor'},
        {'name': 'Monika Beňová'}
    ]
    resp = vpapi.post('people', mps)
    id1 = resp[1]['id']
    vpapi.patch('people/%s' % id1, {'name': 'Monika Flašíková-Beňová'}, effective_date='2006-05-20')
    mp1 = vpapi.get('people/%s' % id1)
    print(mp1)

Don't forget to download `server certificate`_ to communicate with the API by HTTPS. Ensure that ``SERVER_CERT`` variable in the client module code points to the file with certificate.

.. _`server certificate`: https://github.com/KohoVolit/api.parldata.eu/tree/master/client
