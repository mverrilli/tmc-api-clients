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


class RunConfig(object):
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
        'trigger': 'Trigger',
        'runtime': 'Runtime'
    }

    attribute_map = {
        'trigger': 'trigger',
        'runtime': 'runtime'
    }

    def __init__(self, trigger=None, runtime=None):  # noqa: E501
        """RunConfig - a model defined in Swagger"""  # noqa: E501

        self._trigger = None
        self._runtime = None
        self.discriminator = None

        if trigger is not None:
            self.trigger = trigger
        if runtime is not None:
            self.runtime = runtime

    @property
    def trigger(self):
        """Gets the trigger of this RunConfig.  # noqa: E501


        :return: The trigger of this RunConfig.  # noqa: E501
        :rtype: Trigger
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this RunConfig.


        :param trigger: The trigger of this RunConfig.  # noqa: E501
        :type: Trigger
        """

        self._trigger = trigger

    @property
    def runtime(self):
        """Gets the runtime of this RunConfig.  # noqa: E501


        :return: The runtime of this RunConfig.  # noqa: E501
        :rtype: Runtime
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this RunConfig.


        :param runtime: The runtime of this RunConfig.  # noqa: E501
        :type: Runtime
        """

        self._runtime = runtime

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
        if issubclass(RunConfig, dict):
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
        if not isinstance(other, RunConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other