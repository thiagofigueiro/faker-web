# -*- coding: utf-8 -*-
from faker.providers import BaseProvider

from .mimetypes import mime_types


class WebProvider(BaseProvider):
    """
    A Provider for web-related test data.

    >>> from faker import Faker
    >>> from faker_web import WebProvider
    >>> fake = Faker()
    >>> fake.add_provider(WebProvider)
    """
    all_mime_types = mime_types

    popular_mime_types = {
        'application/javascript': ['js'],
        'application/json': ['json'],
        'application/pdf': ['pdf'],
        'image/jpeg': ['jpeg', 'jpg', 'jpe'],
        'image/gif': ['gif'],
        'image/png': ['png'],
        'image/svg+xml': ['svg', 'svgz'],
        'text/css': ['css'],
        'text/html': ['html', 'htm'],
        'text/plain': ['txt', 'text', 'conf', 'def', 'list', 'log', 'in'],
    }

    def mime_type(self):
        """
        Returns a mime-type from the list of types understood by the Apache
        http server.

        >>> fake.mime_type()
        application/mxf

        :return: content-type/mime-type
        :rtype: str
        """
        return self.random_element(self.all_mime_types.keys())

    def mime_type_popular(self):
        """
        Returns a popular mime-type.

        >>> fake.mime_type_popular()
        text/html

        :return: content-type/mime-type
        :rtype: str
        """
        return self.random_element(self.popular_mime_types.keys())
