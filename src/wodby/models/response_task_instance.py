# coding: utf-8

"""
    Wodby API Client

    Wodby Developer Documentation https://wodby.com/docs/dev  # noqa: E501

    OpenAPI spec version: 3.0.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wodby.models.instance import Instance  # noqa: F401,E501
from wodby.models.task import Task  # noqa: F401,E501


class ResponseTaskInstance(object):
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
        'instance': 'Instance',
        'task': 'Task'
    }

    attribute_map = {
        'instance': 'instance',
        'task': 'task'
    }

    def __init__(self, instance=None, task=None):  # noqa: E501
        """ResponseTaskInstance - a model defined in Swagger"""  # noqa: E501

        self._instance = None
        self._task = None
        self.discriminator = None

        self.instance = instance
        self.task = task

    @property
    def instance(self):
        """Gets the instance of this ResponseTaskInstance.  # noqa: E501


        :return: The instance of this ResponseTaskInstance.  # noqa: E501
        :rtype: Instance
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this ResponseTaskInstance.


        :param instance: The instance of this ResponseTaskInstance.  # noqa: E501
        :type: Instance
        """
        if instance is None:
            raise ValueError("Invalid value for `instance`, must not be `None`")  # noqa: E501

        self._instance = instance

    @property
    def task(self):
        """Gets the task of this ResponseTaskInstance.  # noqa: E501


        :return: The task of this ResponseTaskInstance.  # noqa: E501
        :rtype: Task
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this ResponseTaskInstance.


        :param task: The task of this ResponseTaskInstance.  # noqa: E501
        :type: Task
        """
        if task is None:
            raise ValueError("Invalid value for `task`, must not be `None`")  # noqa: E501

        self._task = task

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
        if issubclass(ResponseTaskInstance, dict):
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
        if not isinstance(other, ResponseTaskInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
