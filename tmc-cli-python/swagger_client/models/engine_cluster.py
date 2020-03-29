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


class EngineCluster(object):
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
        'workspace': 'WorkspaceInfo',
        'create_date': 'datetime',
        'update_date': 'datetime',
        'runtime_id': 'str',
        'availability': 'str',
        'engines': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'workspace': 'workspace',
        'create_date': 'createDate',
        'update_date': 'updateDate',
        'runtime_id': 'runtimeId',
        'availability': 'availability',
        'engines': 'engines'
    }

    def __init__(self, id=None, name=None, description=None, workspace=None, create_date=None, update_date=None, runtime_id=None, availability=None, engines=None):  # noqa: E501
        """EngineCluster - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._workspace = None
        self._create_date = None
        self._update_date = None
        self._runtime_id = None
        self._availability = None
        self._engines = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if workspace is not None:
            self.workspace = workspace
        self.create_date = create_date
        if update_date is not None:
            self.update_date = update_date
        self.runtime_id = runtime_id
        if availability is not None:
            self.availability = availability
        if engines is not None:
            self.engines = engines

    @property
    def id(self):
        """Gets the id of this EngineCluster.  # noqa: E501

        Resource id  # noqa: E501

        :return: The id of this EngineCluster.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EngineCluster.

        Resource id  # noqa: E501

        :param id: The id of this EngineCluster.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this EngineCluster.  # noqa: E501

        Resource name  # noqa: E501

        :return: The name of this EngineCluster.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EngineCluster.

        Resource name  # noqa: E501

        :param name: The name of this EngineCluster.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this EngineCluster.  # noqa: E501

        Resource description  # noqa: E501

        :return: The description of this EngineCluster.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EngineCluster.

        Resource description  # noqa: E501

        :param description: The description of this EngineCluster.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def workspace(self):
        """Gets the workspace of this EngineCluster.  # noqa: E501

        Resource workspace  # noqa: E501

        :return: The workspace of this EngineCluster.  # noqa: E501
        :rtype: WorkspaceInfo
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this EngineCluster.

        Resource workspace  # noqa: E501

        :param workspace: The workspace of this EngineCluster.  # noqa: E501
        :type: WorkspaceInfo
        """

        self._workspace = workspace

    @property
    def create_date(self):
        """Gets the create_date of this EngineCluster.  # noqa: E501

        Date of creation of the resource  # noqa: E501

        :return: The create_date of this EngineCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this EngineCluster.

        Date of creation of the resource  # noqa: E501

        :param create_date: The create_date of this EngineCluster.  # noqa: E501
        :type: datetime
        """
        if create_date is None:
            raise ValueError("Invalid value for `create_date`, must not be `None`")  # noqa: E501

        self._create_date = create_date

    @property
    def update_date(self):
        """Gets the update_date of this EngineCluster.  # noqa: E501

        Date of updating of the resource  # noqa: E501

        :return: The update_date of this EngineCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this EngineCluster.

        Date of updating of the resource  # noqa: E501

        :param update_date: The update_date of this EngineCluster.  # noqa: E501
        :type: datetime
        """

        self._update_date = update_date

    @property
    def runtime_id(self):
        """Gets the runtime_id of this EngineCluster.  # noqa: E501

        Resource runtime id  # noqa: E501

        :return: The runtime_id of this EngineCluster.  # noqa: E501
        :rtype: str
        """
        return self._runtime_id

    @runtime_id.setter
    def runtime_id(self, runtime_id):
        """Sets the runtime_id of this EngineCluster.

        Resource runtime id  # noqa: E501

        :param runtime_id: The runtime_id of this EngineCluster.  # noqa: E501
        :type: str
        """
        if runtime_id is None:
            raise ValueError("Invalid value for `runtime_id`, must not be `None`")  # noqa: E501

        self._runtime_id = runtime_id

    @property
    def availability(self):
        """Gets the availability of this EngineCluster.  # noqa: E501

        Availability status of engine|cluster  # noqa: E501

        :return: The availability of this EngineCluster.  # noqa: E501
        :rtype: str
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this EngineCluster.

        Availability status of engine|cluster  # noqa: E501

        :param availability: The availability of this EngineCluster.  # noqa: E501
        :type: str
        """
        allowed_values = ["AVAILABLE", "NOT_AVAILABLE", "RETIRED"]  # noqa: E501
        if availability not in allowed_values:
            raise ValueError(
                "Invalid value for `availability` ({0}), must be one of {1}"  # noqa: E501
                .format(availability, allowed_values)
            )

        self._availability = availability

    @property
    def engines(self):
        """Gets the engines of this EngineCluster.  # noqa: E501

        Engines in cluster  # noqa: E501

        :return: The engines of this EngineCluster.  # noqa: E501
        :rtype: list[str]
        """
        return self._engines

    @engines.setter
    def engines(self, engines):
        """Sets the engines of this EngineCluster.

        Engines in cluster  # noqa: E501

        :param engines: The engines of this EngineCluster.  # noqa: E501
        :type: list[str]
        """

        self._engines = engines

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
        if issubclass(EngineCluster, dict):
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
        if not isinstance(other, EngineCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
