..
    This file is part of Invenio.
    Copyright (C) 2017 CERN.

    Invenio is free software; you can redistribute it
    and/or modify it under the terms of the GNU General Public License as
    published by the Free Software Foundation; either version 2 of the
    License, or (at your option) any later version.

    Invenio is distributed in the hope that it will be
    useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Invenio; if not, write to the
    Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
    MA 02111-1307, USA.

    In applying this license, CERN does not
    waive the privileges and immunities granted to it by virtue of its status
    as an Intergovernmental Organization or submit itself to any jurisdiction.


Usage
=====

.. automodule:: invenio_queues

[DRAFT] How to declare queues?

- Entrypoints

.. code-block:: python

   'invenio_queues.queues':'example_app.queues.declare_queues'

- Function

.. code-block:: python

   def declare_queues():
       """Index statistics events."""

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
