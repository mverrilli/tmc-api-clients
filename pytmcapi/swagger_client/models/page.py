# coding: utf-8

"""
    Talend Management Console Public API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Page(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'items': 'list[object]',
        'limit': 'int',
        'offset': 'int',
        'total': 'int'
    }

    attribute_map = {
        'items': 'items',
        'limit': 'limit',
        'offset': 'offset',
        'total': 'total'
    }

    def __init__(self, items=None, limit=None, offset=None, total=None):  # noqa: E501
        """Page - a model defined in Swagger"""  # noqa: E501

        self._items = None
        self._limit = None
        self._offset = None
        self._total = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if total is not None:
            self.total = total

    @property
    def items(self):
        """Gets the items of this Page.  # noqa: E501


        :return: The items of this Page.  # noqa: E501
        :rtype: list[object]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Page.


        :param items: The items of this Page.  # noqa: E501
        :type: list[object]
        """

        self._items = items

    @property
    def limit(self):
        """Gets the limit of this Page.  # noqa: E501


        :return: The limit of this Page.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this Page.


        :param limit: The limit of this Page.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this Page.  # noqa: E501


        :return: The offset of this Page.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this Page.


        :param offset: The offset of this Page.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def total(self):
        """Gets the total of this Page.  # noqa: E501


        :return: The total of this Page.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Page.


        :param total: The total of this Page.  # noqa: E501
        :type: int
        """

        self._total = total

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Page, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Page):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
