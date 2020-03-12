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
"""Provide a specific broker_url for queues.

If the variable is not configured it falls back to the default BROKER_URL of
our application.
"""

QUEUES_CONNECTION_POOL = get_connection_pool
"""Default queues connection pool."""
