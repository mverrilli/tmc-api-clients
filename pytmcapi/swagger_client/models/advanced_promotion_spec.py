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


class AdvancedPromotionSpec(object):
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
        'artifact_id': 'str',
        'artifact_type': 'str'
    }

    attribute_map = {
        'artifact_id': 'artifactId',
        'artifact_type': 'artifactType'
    }

    def __init__(self, artifact_id=None, artifact_type=None):  # noqa: E501
        """AdvancedPromotionSpec - a model defined in Swagger"""  # noqa: E501

        self._artifact_id = None
        self._artifact_type = None
        self.discriminator = None

        if artifact_id is not None:
            self.artifact_id = artifact_id
        if artifact_type is not None:
            self.artifact_type = artifact_type

    @property
    def artifact_id(self):
        """Gets the artifact_id of this AdvancedPromotionSpec.  # noqa: E501

        Advanced Promotion Artifact Id  # noqa: E501

        :return: The artifact_id of this AdvancedPromotionSpec.  # noqa: E501
        :rtype: str
        """
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, artifact_id):
        """Sets the artifact_id of this AdvancedPromotionSpec.

        Advanced Promotion Artifact Id  # noqa: E501

        :param artifact_id: The artifact_id of this AdvancedPromotionSpec.  # noqa: E501
        :type: str
        """

        self._artifact_id = artifact_id

    @property
    def artifact_type(self):
        """Gets the artifact_type of this AdvancedPromotionSpec.  # noqa: E501

        Advanced Promotion Artifact Type  # noqa: E501

        :return: The artifact_type of this AdvancedPromotionSpec.  # noqa: E501
        :rtype: str
        """
        return self._artifact_type

    @artifact_type.setter
    def artifact_type(self, artifact_type):
        """Sets the artifact_type of this AdvancedPromotionSpec.

        Advanced Promotion Artifact Type  # noqa: E501

        :param artifact_type: The artifact_type of this AdvancedPromotionSpec.  # noqa: E501
        :type: str
        """
        allowed_values = ["WORKSPACE", "PLAN", "FLOW", "ACTION"]  # noqa: E501
        if artifact_type not in allowed_values:
            raise ValueError(
                "Invalid value for `artifact_type` ({0}), must be one of {1}"  # noqa: E501
                .format(artifact_type, allowed_values)
            )

        self._artifact_type = artifact_type

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
        if issubclass(AdvancedPromotionSpec, dict):
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
        if not isinstance(other, AdvancedPromotionSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
