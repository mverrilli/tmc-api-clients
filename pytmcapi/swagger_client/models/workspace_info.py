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


class WorkspaceInfo(object):
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
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'owner': 'str',
        'type': 'str',
        'environment': 'EnvironmentInfo'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'owner': 'owner',
        'type': 'type',
        'environment': 'environment'
    }

    def __init__(self, id=None, name=None, description=None, owner=None, type=None, environment=None):  # noqa: E501
        """WorkspaceInfo - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._owner = None
        self._type = None
        self._environment = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if owner is not None:
            self.owner = owner
        self.type = type
        if environment is not None:
            self.environment = environment

    @property
    def id(self):
        """Gets the id of this WorkspaceInfo.  # noqa: E501

        Workspace identifier  # noqa: E501

        :return: The id of this WorkspaceInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkspaceInfo.

        Workspace identifier  # noqa: E501

        :param id: The id of this WorkspaceInfo.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this WorkspaceInfo.  # noqa: E501

        Workspace name  # noqa: E501

        :return: The name of this WorkspaceInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkspaceInfo.

        Workspace name  # noqa: E501

        :param name: The name of this WorkspaceInfo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this WorkspaceInfo.  # noqa: E501

        Workspace description  # noqa: E501

        :return: The description of this WorkspaceInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkspaceInfo.

        Workspace description  # noqa: E501

        :param description: The description of this WorkspaceInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def owner(self):
        """Gets the owner of this WorkspaceInfo.  # noqa: E501

        Workspace owner  # noqa: E501

        :return: The owner of this WorkspaceInfo.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this WorkspaceInfo.

        Workspace owner  # noqa: E501

        :param owner: The owner of this WorkspaceInfo.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def type(self):
        """Gets the type of this WorkspaceInfo.  # noqa: E501

        Workspace type  # noqa: E501

        :return: The type of this WorkspaceInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WorkspaceInfo.

        Workspace type  # noqa: E501

        :param type: The type of this WorkspaceInfo.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["shared", "personal", "custom"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def environment(self):
        """Gets the environment of this WorkspaceInfo.  # noqa: E501

        Workspace environment  # noqa: E501

        :return: The environment of this WorkspaceInfo.  # noqa: E501
        :rtype: EnvironmentInfo
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this WorkspaceInfo.

        Workspace environment  # noqa: E501

        :param environment: The environment of this WorkspaceInfo.  # noqa: E501
        :type: EnvironmentInfo
        """

        self._environment = environment

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
        if issubclass(WorkspaceInfo, dict):
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
        if not isinstance(other, WorkspaceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other