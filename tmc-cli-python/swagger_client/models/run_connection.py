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


class RunConnection(object):
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
        'app': 'str',
        'parameters': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'workspace': 'workspace',
        'create_date': 'createDate',
        'update_date': 'updateDate',
        'app': 'app',
        'parameters': 'parameters'
    }

    def __init__(self, id=None, name=None, description=None, workspace=None, create_date=None, update_date=None, app=None, parameters=None):  # noqa: E501
        """RunConnection - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._workspace = None
        self._create_date = None
        self._update_date = None
        self._app = None
        self._parameters = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.workspace = workspace
        self.create_date = create_date
        if update_date is not None:
            self.update_date = update_date
        self.app = app
        self.parameters = parameters

    @property
    def id(self):
        """Gets the id of this RunConnection.  # noqa: E501

        Id of connection  # noqa: E501

        :return: The id of this RunConnection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RunConnection.

        Id of connection  # noqa: E501

        :param id: The id of this RunConnection.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this RunConnection.  # noqa: E501

        Name of connection  # noqa: E501

        :return: The name of this RunConnection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RunConnection.

        Name of connection  # noqa: E501

        :param name: The name of this RunConnection.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this RunConnection.  # noqa: E501

        Description of connection  # noqa: E501

        :return: The description of this RunConnection.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RunConnection.

        Description of connection  # noqa: E501

        :param description: The description of this RunConnection.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def workspace(self):
        """Gets the workspace of this RunConnection.  # noqa: E501

        Workspace of connection  # noqa: E501

        :return: The workspace of this RunConnection.  # noqa: E501
        :rtype: WorkspaceInfo
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this RunConnection.

        Workspace of connection  # noqa: E501

        :param workspace: The workspace of this RunConnection.  # noqa: E501
        :type: WorkspaceInfo
        """
        if workspace is None:
            raise ValueError("Invalid value for `workspace`, must not be `None`")  # noqa: E501

        self._workspace = workspace

    @property
    def create_date(self):
        """Gets the create_date of this RunConnection.  # noqa: E501

        Date of creation of connection  # noqa: E501

        :return: The create_date of this RunConnection.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this RunConnection.

        Date of creation of connection  # noqa: E501

        :param create_date: The create_date of this RunConnection.  # noqa: E501
        :type: datetime
        """
        if create_date is None:
            raise ValueError("Invalid value for `create_date`, must not be `None`")  # noqa: E501

        self._create_date = create_date

    @property
    def update_date(self):
        """Gets the update_date of this RunConnection.  # noqa: E501

        Date of updating of connection  # noqa: E501

        :return: The update_date of this RunConnection.  # noqa: E501
        :rtype: datetime
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this RunConnection.

        Date of updating of connection  # noqa: E501

        :param update_date: The update_date of this RunConnection.  # noqa: E501
        :type: datetime
        """

        self._update_date = update_date

    @property
    def app(self):
        """Gets the app of this RunConnection.  # noqa: E501

        Date of updating of connection  # noqa: E501

        :return: The app of this RunConnection.  # noqa: E501
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this RunConnection.

        Date of updating of connection  # noqa: E501

        :param app: The app of this RunConnection.  # noqa: E501
        :type: str
        """
        if app is None:
            raise ValueError("Invalid value for `app`, must not be `None`")  # noqa: E501

        self._app = app

    @property
    def parameters(self):
        """Gets the parameters of this RunConnection.  # noqa: E501

        Connection parameters  # noqa: E501

        :return: The parameters of this RunConnection.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this RunConnection.

        Connection parameters  # noqa: E501

        :param parameters: The parameters of this RunConnection.  # noqa: E501
        :type: dict(str, str)
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

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
        if issubclass(RunConnection, dict):
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
        if not isinstance(other, RunConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
