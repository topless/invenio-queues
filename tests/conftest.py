# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Pytest configuration."""

from __future__ import absolute_import, print_function

import shutil
import tempfile

import pytest
from celery import current_app as current_celery_app
from flask import Flask
from flask_babelex import Babel
from invenio_queues import InvenioQueues
from kombu import Exchange
from mock import patch


MOCK_MQ_EXCHANGE = Exchange(
    'events',
    type='direct',
    delivery_mode='transient',  # in-memory queue
)


def mock_declare_queues():
    return [dict(name='stats_record_view', exchange=MOCK_MQ_EXCHANGE)]


@pytest.yield_fixture()
def instance_path():
    """Temporary instance path."""
    path = tempfile.mkdtemp()
    yield path
    shutil.rmtree(path)


@pytest.fixture()
def app(instance_path):
    """Flask application fixture."""
    app_ = Flask('testapp')
    app_.config.update(
        SECRET_KEY='SECRET_KEY',
        TESTING=True,
    )
    Babel(app_)
    InvenioQueues(app_)
    return app_


@pytest.yield_fixture()
def queues_app(app):
    """Flask application fixture."""
    app = Flask('queues_app')
    app.config.update(
        SECRET_KEY='SECRET_KEY',
        TESTING=True,
        QUEUES_CONNECTION_POOL=current_celery_app.pool,
    )
    InvenioQueues(app)

    with patch('pkg_resources.EntryPoint') as MockEntryPoint:
        entrypoint = MockEntryPoint('ep1', 'ep2')
        entrypoint.load.return_value = mock_declare_queues
        with patch('invenio_queues.ext.iter_entry_points',
                   return_value=[entrypoint]):
            qs = app.extensions['invenio-queues']
            qs.queues
    return app
