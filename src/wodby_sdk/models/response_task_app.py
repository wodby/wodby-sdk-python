# coding: utf-8

"""
    Wodby API Client

    Wodby Developer Documentation https://wodby.com/docs/dev  # noqa: E501

    OpenAPI spec version: 3.0.1
    Contact: hello@wodby.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wodby_sdk.models.app import App  # noqa: F401,E501
from wodby_sdk.models.task import Task  # noqa: F401,E501


class ResponseTaskApp(object):
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
        'app': 'App',
        'task': 'Task'
    }

    attribute_map = {
        'app': 'app',
        'task': 'task'
    }

    def __init__(self, app=None, task=None):  # noqa: E501
        """ResponseTaskApp - a model defined in Swagger"""  # noqa: E501

        self._app = None
        self._task = None
        self.discriminator = None

        self.app = app
        self.task = task

    @property
    def app(self):
        """Gets the app of this ResponseTaskApp.  # noqa: E501


        :return: The app of this ResponseTaskApp.  # noqa: E501
        :rtype: App
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ResponseTaskApp.


        :param app: The app of this ResponseTaskApp.  # noqa: E501
        :type: App
        """
        if app is None:
            raise ValueError("Invalid value for `app`, must not be `None`")  # noqa: E501

        self._app = app

    @property
    def task(self):
        """Gets the task of this ResponseTaskApp.  # noqa: E501


        :return: The task of this ResponseTaskApp.  # noqa: E501
        :rtype: Task
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this ResponseTaskApp.


        :param task: The task of this ResponseTaskApp.  # noqa: E501
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResponseTaskApp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
