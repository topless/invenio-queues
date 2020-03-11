# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2020 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


r"""Invenio module for managin queues

This guide will show you how to get started with Invenio-Queues. It assumes
that you already have knowledge of Flask applications and Invenio modules.

It will then explain key topics and concepts of this module.

Getting started
---------------

Register queues
^^^^^^^^^^^^^^^

- Entrypoints

.. code-block:: python

   'invenio_queues.queues': 'example_app.queues.declare_queues'

- Function

.. code-block:: python

   from kombu import Exchange

   def declare_queues():

       default_exchange = Exchange(
           'example',
           type='direct',
           delivery_mode='transient',  # in-memory queue
       )

       return [
           dict(
               name='notifications',
               exchange=default_exchange
           ),
           dict(
               name='jobs',
               exchange=default_exchange
           )
       ]

Create queues
^^^^^^^^^^^^^

>>>

Access queues
^^^^^^^^^^^^^

You can list the available queues by using the command line interface

>>> invenio queues list

or programmatically

>>> from invenio_queues.proxies import current_queues
>>> current_queues.queues.key()

Suppose you have a queue with name "my_queue" you can directly access it by name

>>> my_queue = current_queues.queues["my_queue"]


Publish events
^^^^^^^^^^^^^^

After we have defined and instantiated (declare) our Queue we can start using it.
This operation pushes an event or events to the queue:

.. code-block:: python

    # NOTE: publish expects and array of events

    events = [1, 2, 3]
    current_queues.queues["my_queue"].publish(events)


Comsume events
^^^^^^^^^^^^^^

After you have published some events in your queue, you can consume them.
The consume method of the queue will return a generator for the events:

.. code-block:: python

    queue_gen = current_queues.queues["my_queue"].consume()
    list(queue_gen)

"""

from __future__ import absolute_import, print_function

from .ext import InvenioQueues
from .proxies import current_queues
from .version import __version__

__all__ = (
    '__version__',
    'current_queues',
    'InvenioQueues',
)
