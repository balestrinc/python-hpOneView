# -*- coding: utf-8 -*-
###
# (C) Copyright (2012-2016) Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()

__title__ = 'server-profile-template'
__version__ = '0.0.1'
__copyright__ = '(C) Copyright (2012-2016) Hewlett Packard Enterprise Development LP'
__license__ = 'MIT'
__status__ = 'Development'

from hpOneView.resources.resource import ResourceClient


class ServerProfileTemplate(object):
    URI = '/rest/server-profile-templates'

    def __init__(self, con):
        self._connection = con
        self._client = ResourceClient(con, self.URI)

    def get_all(self, start=0, count=-1, filter='', sort=''):
        """
        Gets a list of server profile templates based on optional sorting and filtering, and constrained by start and
        count parameters.

        Args:
            start:
                The first item to return, using 0-based indexing.
                If not specified, the default is 0 - start with the first available item.
            count:
                The number of resources to return.
                Providing a -1 for the count parameter will restrict the result set size to 64 server profile
                templates. The maximum number of profile templates is restricted to 256, i.e., if user requests more
                than 256, this will be internally limited to 256.
                The actual number of items in the response may differ from the
                requested count if the sum of start and count exceed the total number of items, or if returning the
                requested number of items would take too long.
            filter:
                A general filter/query string to narrow the list of items returned. The
                default is no filter - all resources are returned.
                Filters are supported for the name, description, affinity, macType, wwnType, serialNumberType, status,
                serverHardwareTypeUri, enclosureGroupUri, firmware.firmwareBaselineUri attributes.
            sort:
                The sort order of the returned data set. By default, the sort order is based
                on create time, with the oldest entry first.

        Returns:
            list: A list of server profile templates

        """
        return self._client.get_all(start=start, count=count, filter=filter, sort=sort)

    def get(self, id_or_uri):
        """
        Gets a server profile template resource by ID or by uri
        Args:
            id_or_uri: Could be either the server profile template resource id or uri

        Returns:
            dict: The server profile template resource
        """
        return self._client.get(id_or_uri=id_or_uri)

    def get_by(self, field, value):
        """
        Get all server profile templates that matches a specified filter
        The search is case insensitive

        Args:
            field: field name to filter
            value: value to filter

        Returns:
            list: A list of server profile templates
        """
        return self._client.get_by(field, value)

    def get_by_name(self, name):
        """
        Gets a server profile template by name.

        Args:
            name: Name of the server profile template

        Returns:
            dict: The server profile template resource
        """
        return self._client.get_by_name(name)
