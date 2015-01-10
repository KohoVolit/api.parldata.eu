=====
Event
=====

Example of an event is a session, sitting, elections, etc.

---------------------------
1. Use cases & requirements
---------------------------

The Event class should have properties for:

#. the `organization <http://www.popoloproject.com/specs/organization.html>`_ where the event is held
    House of Commons

#. name
    2nd Session

#. identifier
    2

#. type
    e.g. a session, sitting, etc.

#. the time at which the event begins
    October 9, 2013 at 9:00am

#. the time at which the event ends
    October 9, 2013 at 5:57pm

#. parent event
    The 3rd sitting of the 2nd session


-----------------
2. Standard reuse
-----------------

Some research will hopefully appear in Popolo_ soon.

.. _Popolo: http://www.popoloproject.com


-------------------------
3. Classes and properties
-------------------------

+------------+-------+-----------------------------------------------+
|Term        |Mapping|Definition                                     |
+============+=======+===============================================+
|Event       |       |An event is a session, sitting, elections, etc.|
+------------+-------+-----------------------------------------------+
|organization|       |The organization where the event is held       |
+------------+-------+-----------------------------------------------+
|name        |       |Name of the event                              |
+------------+-------+-----------------------------------------------+
|identifier  |       |An issued identifier, e.g. a sequential number |
+------------+-------+-----------------------------------------------+
|type        |       |Type of the event                              |
+------------+-------+-----------------------------------------------+
|start date  |       |The time at which the event begins             |
+------------+-------+-----------------------------------------------+
|end date    |       |The time at which the event ends               |
+------------+-------+-----------------------------------------------+
|parent      |       |The event this event is part of                |
+------------+-------+-----------------------------------------------+


----------------
4. Serialization
----------------

JSON
====

.. code-block:: json

    {
      "id": "session-2-sitting-3",
      "organization_id": "legislative-council-of-hong-kong",
      "name": "The 3rd Sitting of the 2nd Session",
      "identifier": "3",
      "type": "sitting",
      "start_date": "2013-10-09T09:00:00Z",
      "end_date": "2013-10-09T17:57:10Z",
      "parent_id": "session-2"
    }


JSON schema
===========

.. code-block:: json

    {
      "$schema": "http://json-schema.org/draft-03/schema#",
      "id": "http://www.popoloproject.com/schemas/event.json#",
      "title": "Event",
      "description": "An event is a e.g. a session, sitting, elections, etc.",
      "type": "object",
      "properties": {
        "id": {
          "description": "The event's unique identifier",
          "type": ["string", "null"]
        },
        "organization_id": {
          "description": "The ID of the organization where the event is held",
          "type": ["string", "null"]
        },
        "organization": {
          "description": "The organization where the event is held ",
          "$ref": "http://www.popoloproject.com/schemas/organization.json#"
        },
        "name": {
            "description": "Name of the event",
            "type": ["string", "null"]
        },
        "identifier": {
          "description": "An issued identifier",
          "type": ["string", "null"]
        },
        "type": {
          "description": "Type of the event",
          "type": ["string", "null"]
        },
        "start_date": {
          "description": "The time at which the event begins",
          "type": ["string", "null"],
          "format": "date-time"
        },
        "end_date": {
          "description": "The time at which the event ends",
          "type": ["string", "null"],
          "format": "date-time"
        },
        "parent_id": {
          "description": "The ID of the event this event is part of",
          "type": ["string", "null"]
        },
        "parent": {
          "description": "The event this event is part of",
          "$ref": "http://www.popoloproject.com/schemas/event.json#"
        },
        "created_at": {
          "description": "The time at which the resource was created",
          "type": ["string", "null"],
          "format": "date-time"
        },
        "updated_at": {
          "description": "The time at which the resource was last modified",
          "type": ["string", "null"],
          "format": "date-time"
        },
        "sources": {
          "description": "URLs to documents from which the resource is derived",
          "type": "array",
          "items": {
            "$ref": "http://www.popoloproject.com/schemas/link.json#"
          }
        }
      }
    }


-------------
5. Code lists
-------------

Result
======

Implementations may use values from outside this list to reflect the diversity of event types.

* ``session``
* ``sitting``
* ``other``
