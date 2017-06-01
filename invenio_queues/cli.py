# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016 CERN.
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

"""CLI for Invenio-Stats."""

from __future__ import absolute_import, print_function

import click
from flask import current_app
from flask.cli import with_appcontext
from invenio_search.cli import index
from pkg_resources import iter_entry_points
from .proxies import current_queues


@index.group(chain=True)
def queues():
    """Manage events queue."""


@queues.command('init')
@with_appcontext
def init():
    """Initialize indexing queue."""
    import ipdb
    ipdb.set_trace()
    current_queues.declare()
    click.secho('Queue has been initialized.', fg='green')


@queues.command('purge')
@with_appcontext
def purge_queue():
    """Purge indexing queue."""
    current_queues.purge()
    click.secho('Queue has been purged.', fg='green')


@queues.command('delete')
@with_appcontext
def delete_queue():
    """Delete indexing queue."""
    current_queues.delete()
    click.secho('Queue has been deleted.', fg='green')
