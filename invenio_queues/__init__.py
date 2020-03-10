# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2020 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


r"""Invenio module for managing queues.

This guide will show you how to get started with Invenio-Queues. It assumes
that you already have knowledge of Flask applications and Invenio modules.

It will then explain key topics and concepts of this module.

Getting started
---------------

You will learn how to register queues and to interact with it. To begin with,
you need to setup your virtual environment and install this module.

You need an application to work with, that can be created with the following
commands in a Python shell:

>>> from flask import current_app

You can then initialize the module:

>>> from invenio_queues.ext import InvenioQueues
>>> ext_queues = InvenioQueues(app)

In our example, we are using RabbitMQ as a broker, which can be configured
as follow:

>>> current_app.config['QUEUES_BROKER_URL'] = 'amqp://localhost:5672'

Register queues
^^^^^^^^^^^^^^^

To register queues, you need to start by creating an exchange for the queues:

.. code-block:: python

   from kombu import Exchange

   default_exchange = Exchange(
       'example',
       type='direct',
       delivery_mode='transient',  # in-memory queue
   )

You can now configure the queues as followed:

.. code-block:: python

   from invenio_queues.proxies import current_queues
   from invenio_queues.queue import Queue

   current_queues.queues = dict()
   connection_pool = current_app.config.get('QUEUES_CONNECTION_POOL')

   current_queues.queues['notifications'] = Queue(
       default_exchange,
       'notifications',
       connection_pool
   )

   current_queues.queues['jobs'] = Queue(
       default_exchange,
       'jobs',
       connection_pool
   )

Create queues
^^^^^^^^^^^^^

Now that the queues are configured, you can create them:

>>> current_queues.declare()

If you want to delete them, this can be done in the same way:

>>> current_queues.delete()

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
