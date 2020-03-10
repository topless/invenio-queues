# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017-2020 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Default configuration for QUEUES."""

from .utils import get_connection_pool

QUEUES_BROKER_URL = None
"""Allow invenio-queues to have a different broker than the Celery."""

QUEUES_CONNECTION_POOL = get_connection_pool
"""Default queues connection pool."""
