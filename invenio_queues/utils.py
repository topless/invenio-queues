# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017-2020 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio Queues utility functions."""

from flask import current_app
from kombu import Connection
from kombu.pools import connections


def get_connection_pool():
    """Retrieve the broker connection pool.

    Note: redis is not supported as "queue.exists" doesn't behave the same
    way.
    """
    return connections[Connection(
        # Allow invenio-queues to have a different broker than the Celery one
        current_app.config.get('QUEUES_BROKER_URL',
                               # otherwise use Celery's BROKER_URL
                               current_app.config.get('BROKER_URL', 'amqp://'))
    )]
