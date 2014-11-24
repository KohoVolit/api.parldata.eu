========================
Visegrad+ parliament API
========================

Visegrad+ parliament API is a `RESTful API`_ providing parliament data from Visegrad and Balkan countries. The data are served in a machine readable format convenient to use in applications or research. The API is public.

.. _`RESTful API`: http://en.wikipedia.org/wiki/Representational_state_transfer#Applied_to_web_services

The API allows also to modify or delete the data to authenticated users (see USAGE_).

.. _USAGE: USAGE.rst

.. contents:: :backlinks: none

-------
Example
-------

To get a list of all Slovak parliament committees make a HTTP request to:

`<http://api.parldata.eu/sk/nrsr/organizations?where={"classification":"committee"}>`_

and you get the data as a JSON_ document.

.. _JSON: http://en.wikipedia.org/wiki/JSON

-----
Usage
-----

A general pattern of API URLs is

::

    http://api.parldata.eu/<country-code>/<parliament-code>/<data-collection>?<parameters>

to find all items satisfying given criteria or

::

    http://api.parldata.eu/<country-code>/<parliament-code>/<data-collection>/<id>?<parameters>

to get a particular item by its *id* value.

Available parliaments
=====================

+---------------+--------------------+------------+---------------+
|Country        |Parliament (chamber)|Country code|Parliament code|
+===============+====================+============+===============+
|Slovakia       |`Národná rada`_     |sk          |nrsr           |
+---------------+--------------------+------------+---------------+
|Czech republic |Poslanecká sněmovna |cz          |psp            |
+---------------+--------------------+------------+---------------+
|Czech republic |Senát               |cz          |senat          |
+---------------+--------------------+------------+---------------+
|example country|example parliament  |xx          |example        |
+---------------+--------------------+------------+---------------+

.. _`Národná rada`: http://api.parldata.eu/sk/nrsr/

Available data collections
==========================

+---------------+-------------------------------------------------------------------------------+
|Collection name|Description                                                                    |
+===============+===============================================================================+
|people_        |Members of parliament and other related people.                                |
+---------------+-------------------------------------------------------------------------------+
|organizations_ |Groups in parliament (e.g. committees) and other organizations.                |
+---------------+-------------------------------------------------------------------------------+
|memberships_   |Memberships of the people in organizations.                                    |
+---------------+-------------------------------------------------------------------------------+
|posts_         |Posts in organizations that can be holded by people.                           |
+---------------+-------------------------------------------------------------------------------+
|motions_       |A motion is "a formal step to introduce a matter for consideration by a group."|
+---------------+-------------------------------------------------------------------------------+
|`vote-events`_ |A vote event is an event at which people's votes are recorded.                 |
+---------------+-------------------------------------------------------------------------------+
|votes_         |A vote is one voter's vote in a vote event.                                    |
+---------------+-------------------------------------------------------------------------------+
|areas_         |Constituencies and other geographic areas whose geometry may change over time. |
+---------------+-------------------------------------------------------------------------------+
|speeches_      |Parts of a debate transcripts - speeches, scenes, narratives or other.         |
+---------------+-------------------------------------------------------------------------------+
|events         |Event (e.g. sessions, sittings, elections, etc.) Not in Popolo yet.            |
+---------------+-------------------------------------------------------------------------------+
|logs_          |Information about updates of the data by scrapers. (Not a part of Popolo.)     |
+---------------+-------------------------------------------------------------------------------+

.. _people: http://www.popoloproject.com/schemas/person.json#
.. _organizations: http://www.popoloproject.com/schemas/organization.json#
.. _memberships: http://www.popoloproject.com/schemas/membership.json#
.. _posts: http://www.popoloproject.com/schemas/post.json#
.. _areas: http://www.popoloproject.com/schemas/area.json#
.. _motions: http://www.popoloproject.com/schemas/motion.json#
.. _`vote-events`: http://www.popoloproject.com/schemas/vote_event.json#
.. _votes: http://www.popoloproject.com/schemas/vote.json#
.. _speeches: http://www.popoloproject.com/schemas/speech.json#
.. _logs: https://github.com/KohoVolit/visegrad-parliament-api/blob/master/schemas/log.py

The collections conform to `Popolo specification`_, links on collection names refer to their schemas.

.. _`Popolo specification`: http://www.popoloproject.com

Parameters
==========

Parameters are used to query a collection and to adjust how the result is returned. They are specified in the URL query component as ``?param1=value1&param2=value2&...`` All parameters are optional.

where
-----

Parameter *where* specifies a condition which items to return. Examples:

* `/sk/nrsr/people?where={"name": "Vladimír Mečiar"} <http://api.parldata.eu/sk/nrsr/people?where={"name": "Vladimír%20Mečiar"}>`_

* `/sk/nrsr/organizations?where={"founding_date": {"$gte": "2012-03-13"}} <http://api.parldata.eu/sk/nrsr/organizations?where={"founding_date": {"$gte": "2012-03-13"}}>`_

* `/sk/nrsr/people?where={"gender": "female", "national_identity": {"$ne": "slovenská"}} <http://api.parldata.eu/sk/nrsr/people?where={"gender": "female", "national_identity": {"$ne": "slovenská"}}>`_

* `/sk/nrsr/organizations?where={"$or": [{"dissolution_date": {"$gte": "2014-03-13"}}, {"dissolution_date": {"$exists": false}}]} <http://api.parldata.eu/sk/nrsr/organizations?where={"$or": [{"dissolution_date": {"$gte": "2014-03-13"}}, {"dissolution_date": {"$exists": false}}]}>`_

* `/sk/nrsr/people?where={"given_name": {"$in": ["Peter", "Pavol"]}} <http://api.parldata.eu/sk/nrsr/people?where={"given_name": {"$in": ["Peter", "Pavol"]}}>`_

* `/sk/nrsr/motions?where={"text": {"$regex": "európsk.*", "$options": "i"}} <http://api.parldata.eu/sk/nrsr/motions?where={"text": {"$regex": "európsk.*", "$options": "i"}}>`_

* `/sk/nrsr/people?where={"identifiers.identifier": "140", "identifiers.scheme": "nrsr.sk"} <http://api.parldata.eu/sk/nrsr/people?where={"identifiers.identifier": "140", "identifiers.scheme": "nrsr.sk"}>`_

* `/sk/nrsr/people?where={"identifiers": {"$elemMatch": {"identifier": "140", "scheme": "nrsr.sk"}}} <http://api.parldata.eu/sk/nrsr/people?where={"identifiers": {"$elemMatch": {"identifier": "140", "scheme": "nrsr.sk"}}}>`_

Notes. Returned items are those where all given conditions are met. *$gte* means greater-or-equal-than, *$ne* is non-equal operator. The last two examples query the list of person's identifiers for a given pair and they are both equivalent.

The *where* parameter uses MongoDB syntax, see `MongoDB operators`_ for full reference.

.. _`MongoDB operators`: http://docs.mongodb.org/manual/reference/operator/query/

**Important note.** When querying for subdocuments, do not use `MongoDB exact match on subdocument syntax`_ – it depends on the order of fields in the subdocument which is undefined. Use `dot notation`_ on particular fields instead or `$elemMatch operator`_ in case of an array of subdocuments as is used in the last two examples.

.. _`MongoDB exact match on subdocument syntax`: http://docs.mongodb.org/manual/tutorial/query-documents/#exact-match-on-the-embedded-document
.. _`dot notation`: http://docs.mongodb.org/manual/tutorial/query-documents/#equality-match-on-fields-within-an-embedded-document
.. _`$elemMatch operator`: http://docs.mongodb.org/manual/tutorial/query-documents/#match-multiple-fields

projection
----------

The *projection* parameter allows to return the given fields only or to exclude specified fields from the result. All fields are returned if the projection is not used. Examples:

* `/sk/nrsr/people?projection={"name": 1, "classification": 1} <http://api.parldata.eu/sk/nrsr/people?projection={"name": 1, "classification": 1}>`_

* `/cz/psp/posts?projection={"contact_details": 0} <http://api.parldata.eu/cz/psp/posts?projection={"contact_details": 0}>`_

Projection allows to reduce transferred data to the fields you really need. Fields *id*, *created_at*, *updated_at* are included in the result regardless of the projection. Mixed inclusive-exclusive projection is not allowed.

sort
----

Ordering of the result. Example:

* `/sk/nrsr/people?sort=[("family_name", -1), ("given_name", -1)] <http://api.parldata.eu/sk/nrsr/people?sort=[("family_name", -1), ("given_name", -1)]>`_

embed
------

Parameter *embed* allows to embed items referenced by the selected ones into the result instead of their *id*-s. See `Embedded JSON documents`_ in Popolo specification. Nested embedded relations are separated by dot. Examples:

.. _`Embedded JSON documents`: http://www.popoloproject.com/specs/#embedded-json-documents

* `/sk/nrsr/organizations/505bd76785ebb509fc183733?embed=["parent", "memberships.person"] <http://api.parldata.eu/sk/nrsr/organizations/505bd76785ebb509fc183733?embed=["parent", "memberships.person"]>`_

* `/sk/nrsr/people/4cdfb11e1f3c000000007822?embed=["memberships.organization"] <http://api.parldata.eu/sk/nrsr/people/4cdfb11e1f3c000000007822?embed=["memberships.organization"]>`_

The former includes all members of the organization into the result as well its parent organization, the latter includes all organizations the person is a member of. It is much more convenient than querying members one by one by *organization_id*.

Maximum level of nested embedding is 3 levels and an item cannot be embedded into itself recursively. Fields of embedded items cannot be used in the *where* parameter.

page, max_results
-----------------

The returned data are paginated to prevent excessive responses. The number of pages of the result can be found in the *_links* field. You can request a particular page of the result using *page* parameter and set number of results per page by *max_results* parameter. The default for *max_results* is 25, maximum allowed value is 50.

Other notes
===========

Each API response provides meta-information besides the data. The resulting data are stored in field *_items*. Field *_links* contains links to other pages of the result.

The default format of the response is JSON as specified in Popolo. You can request XML by sending *Accept: application/xml* in request header, nevertheless Popolo does not define serialization of the data to XML.

Historical changes in the data are tracked by the API. Former values of the properties are stored in the *changes* property.

-------------
Client module
-------------

Instead of sending HTTP requests yourself you can use a client module for Python. Example of usage:

.. code-block:: Python

    import vpapi
    vpapi.parliament('sk/nrsr')

    o = vpapi.get('organizations/505bd76785ebb509fc183733')
    p = vpapi.get('people', page=2)
    vm = vpapi.get('people',
        where={'name': 'Vladimír Mečiar'},
        embed=['memberships.organization'])

To use the client module *vpapi*, make sure you have requests_ package installed in Python, then download the *vpapi* module here_.

.. _requests: http://docs.python-requests.org/en/latest/

.. _here: https://raw.githubusercontent.com/KohoVolit/visegrad-parliament-api/master/client/vpapi.py
