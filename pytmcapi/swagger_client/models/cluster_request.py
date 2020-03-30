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


class ClusterRequest(object):
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
        'name': 'str',
        'workspace_id': 'str',
        'environment_id': 'str',
        'description': 'str',
        'remote_engines': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'workspace_id': 'workspaceId',
        'environment_id': 'environmentId',
        'description': 'description',
        'remote_engines': 'remoteEngines'
    }

    def __init__(self, name=None, workspace_id=None, environment_id=None, description=None, remote_engines=None):  # noqa: E501
        """ClusterRequest - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._workspace_id = None
        self._environment_id = None
        self._description = None
        self._remote_engines = None
        self.discriminator = None

        self.name = name
        self.workspace_id = workspace_id
        self.environment_id = environment_id
        self.description = description
        self.remote_engines = remote_engines

    @property
    def name(self):
        """Gets the name of this ClusterRequest.  # noqa: E501

        Cluster name  # noqa: E501

        :return: The name of this ClusterRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterRequest.

        Cluster name  # noqa: E501

        :param name: The name of this ClusterRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ClusterRequest.  # noqa: E501

        Workspace identifier  # noqa: E501

        :return: The workspace_id of this ClusterRequest.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ClusterRequest.

        Workspace identifier  # noqa: E501

        :param workspace_id: The workspace_id of this ClusterRequest.  # noqa: E501
        :type: str
        """
        if workspace_id is None:
            raise ValueError("Invalid value for `workspace_id`, must not be `None`")  # noqa: E501

        self._workspace_id = workspace_id

    @property
    def environment_id(self):
        """Gets the environment_id of this ClusterRequest.  # noqa: E501

        Environment identifier  # noqa: E501

        :return: The environment_id of this ClusterRequest.  # noqa: E501
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this ClusterRequest.

        Environment identifier  # noqa: E501

        :param environment_id: The environment_id of this ClusterRequest.  # noqa: E501
        :type: str
        """
        if environment_id is None:
            raise ValueError("Invalid value for `environment_id`, must not be `None`")  # noqa: E501

        self._environment_id = environment_id

    @property
    def description(self):
        """Gets the description of this ClusterRequest.  # noqa: E501

        Cluster description  # noqa: E501

        :return: The description of this ClusterRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClusterRequest.

        Cluster description  # noqa: E501

        :param description: The description of this ClusterRequest.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def remote_engines(self):
        """Gets the remote_engines of this ClusterRequest.  # noqa: E501

        List of remote engine ids  # noqa: E501

        :return: The remote_engines of this ClusterRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._remote_engines

    @remote_engines.setter
    def remote_engines(self, remote_engines):
        """Sets the remote_engines of this ClusterRequest.

        List of remote engine ids  # noqa: E501

        :param remote_engines: The remote_engines of this ClusterRequest.  # noqa: E501
        :type: list[str]
        """
        if remote_engines is None:
            raise ValueError("Invalid value for `remote_engines`, must not be `None`")  # noqa: E501

        self._remote_engines = remote_engines

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
        if issubclass(ClusterRequest, dict):
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
        if not isinstance(other, ClusterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other