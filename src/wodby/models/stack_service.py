# coding: utf-8

"""
    Wodby API Client

    Wodby Developer Documentation https://wodby.com/docs/dev  # noqa: E501

    OpenAPI spec version: 3.0.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wodby.models.stack_service_implementation import StackServiceImplementation  # noqa: F401,E501


class StackService(object):
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
        'default': 'bool',
        'id': 'str',
        'implementations': 'list[StackServiceImplementation]',
        'name': 'str',
        'required': 'bool',
        'title': 'str'
    }

    attribute_map = {
        'default': 'default',
        'id': 'id',
        'implementations': 'implementations',
        'name': 'name',
        'required': 'required',
        'title': 'title'
    }

    def __init__(self, default=None, id=None, implementations=None, name=None, required=None, title=None):  # noqa: E501
        """StackService - a model defined in Swagger"""  # noqa: E501

        self._default = None
        self._id = None
        self._implementations = None
        self._name = None
        self._required = None
        self._title = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if id is not None:
            self.id = id
        if implementations is not None:
            self.implementations = implementations
        if name is not None:
            self.name = name
        if required is not None:
            self.required = required
        if title is not None:
            self.title = title

    @property
    def default(self):
        """Gets the default of this StackService.  # noqa: E501


        :return: The default of this StackService.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this StackService.


        :param default: The default of this StackService.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def id(self):
        """Gets the id of this StackService.  # noqa: E501


        :return: The id of this StackService.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StackService.


        :param id: The id of this StackService.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def implementations(self):
        """Gets the implementations of this StackService.  # noqa: E501


        :return: The implementations of this StackService.  # noqa: E501
        :rtype: list[StackServiceImplementation]
        """
        return self._implementations

    @implementations.setter
    def implementations(self, implementations):
        """Sets the implementations of this StackService.


        :param implementations: The implementations of this StackService.  # noqa: E501
        :type: list[StackServiceImplementation]
        """

        self._implementations = implementations

    @property
    def name(self):
        """Gets the name of this StackService.  # noqa: E501


        :return: The name of this StackService.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StackService.


        :param name: The name of this StackService.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def required(self):
        """Gets the required of this StackService.  # noqa: E501


        :return: The required of this StackService.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this StackService.


        :param required: The required of this StackService.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def title(self):
        """Gets the title of this StackService.  # noqa: E501


        :return: The title of this StackService.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this StackService.


        :param title: The title of this StackService.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(StackService, dict):
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
        if not isinstance(other, StackService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
