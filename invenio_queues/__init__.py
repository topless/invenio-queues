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

   'invenio_queues.queues':'example_app.queues.declare_queues'

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

>>> queues list

Publish queues
^^^^^^^^^^^^^^

>>>

Comsume queues
^^^^^^^^^^^^^^

>>>

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
