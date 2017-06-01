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

"""Module tests."""

from __future__ import absolute_import, print_function

from flask import Flask
from flask.cli import ScriptInfo
from click.testing import CliRunner
from invenio_queues import InvenioQueues
import pkg_resources
from mock import MagicMock, Mock, patch


def test_declare():
    with patch('pkg_resources.EntryPoint') as MockEntryPoint:
        # Test that the CLI command succeeds when the entrypoint does
        # return a function.
        runner = CliRunner()

        entrypoint = MockEntryPoint('ep1', 'ep1')
        entrypoint.load.return_value = MagicMock()
        with patch('invenio_queues.cli.iter_entry_points',
                   return_value=[entrypoint]):
            result = runner.invoke(
                instance, ['migrate-secret-key', '--old-key',
                           'OLD_SECRET_KEY'],
                obj=script_info)
            assert result.exit_code == 0
            assert entrypoint.load.called
            entrypoint.load.return_value.assert_called_with(
                old_key='OLD_SECRET_KEY'
            )
            assert 'Successfully changed secret key.' in result.output
