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


class Webhook(object):
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
        'description': 'str',
        'trigger_calls': 'int',
        'trigger_timeout': 'int',
        'run_as_user': 'str',
        'new_url': 'bool',
        'url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'trigger_calls': 'triggerCalls',
        'trigger_timeout': 'triggerTimeout',
        'run_as_user': 'runAsUser',
        'new_url': 'newUrl',
        'url': 'url'
    }

    def __init__(self, name=None, description=None, trigger_calls=None, trigger_timeout=None, run_as_user=None, new_url=None, url=None):  # noqa: E501
        """Webhook - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._trigger_calls = None
        self._trigger_timeout = None
        self._run_as_user = None
        self._new_url = None
        self._url = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if trigger_calls is not None:
            self.trigger_calls = trigger_calls
        if trigger_timeout is not None:
            self.trigger_timeout = trigger_timeout
        if run_as_user is not None:
            self.run_as_user = run_as_user
        if new_url is not None:
            self.new_url = new_url
        if url is not None:
            self.url = url

    @property
    def name(self):
        """Gets the name of this Webhook.  # noqa: E501

        Webhook name  # noqa: E501

        :return: The name of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Webhook.

        Webhook name  # noqa: E501

        :param name: The name of this Webhook.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Webhook.  # noqa: E501

        Webhook description  # noqa: E501

        :return: The description of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Webhook.

        Webhook description  # noqa: E501

        :param description: The description of this Webhook.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def trigger_calls(self):
        """Gets the trigger_calls of this Webhook.  # noqa: E501

        Endpoint call count to run task|plan   # noqa: E501

        :return: The trigger_calls of this Webhook.  # noqa: E501
        :rtype: int
        """
        return self._trigger_calls

    @trigger_calls.setter
    def trigger_calls(self, trigger_calls):
        """Sets the trigger_calls of this Webhook.

        Endpoint call count to run task|plan   # noqa: E501

        :param trigger_calls: The trigger_calls of this Webhook.  # noqa: E501
        :type: int
        """

        self._trigger_calls = trigger_calls

    @property
    def trigger_timeout(self):
        """Gets the trigger_timeout of this Webhook.  # noqa: E501

        Time after which the task will starts from the moment the endpoint is first called   # noqa: E501

        :return: The trigger_timeout of this Webhook.  # noqa: E501
        :rtype: int
        """
        return self._trigger_timeout

    @trigger_timeout.setter
    def trigger_timeout(self, trigger_timeout):
        """Sets the trigger_timeout of this Webhook.

        Time after which the task will starts from the moment the endpoint is first called   # noqa: E501

        :param trigger_timeout: The trigger_timeout of this Webhook.  # noqa: E501
        :type: int
        """

        self._trigger_timeout = trigger_timeout

    @property
    def run_as_user(self):
        """Gets the run_as_user of this Webhook.  # noqa: E501

        The user on behalf of whom the task will be launched  # noqa: E501

        :return: The run_as_user of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._run_as_user

    @run_as_user.setter
    def run_as_user(self, run_as_user):
        """Sets the run_as_user of this Webhook.

        The user on behalf of whom the task will be launched  # noqa: E501

        :param run_as_user: The run_as_user of this Webhook.  # noqa: E501
        :type: str
        """

        self._run_as_user = run_as_user

    @property
    def new_url(self):
        """Gets the new_url of this Webhook.  # noqa: E501

        Indicates whether to generate new url  # noqa: E501

        :return: The new_url of this Webhook.  # noqa: E501
        :rtype: bool
        """
        return self._new_url

    @new_url.setter
    def new_url(self, new_url):
        """Sets the new_url of this Webhook.

        Indicates whether to generate new url  # noqa: E501

        :param new_url: The new_url of this Webhook.  # noqa: E501
        :type: bool
        """

        self._new_url = new_url

    @property
    def url(self):
        """Gets the url of this Webhook.  # noqa: E501

        Webhook url  # noqa: E501

        :return: The url of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Webhook.

        Webhook url  # noqa: E501

        :param url: The url of this Webhook.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(Webhook, dict):
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
        if not isinstance(other, Webhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other