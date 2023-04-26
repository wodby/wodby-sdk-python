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

from wodby.models.stack_service import StackService  # noqa: F401,E501


class Stack(object):
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
        'created': 'int',
        'id': 'str',
        'new_version': 'str',
        'org_id': 'str',
        'revision_number': 'int',
        'services': 'list[StackService]',
        'title': 'str',
        'updated': 'int',
        'version': 'str'
    }

    attribute_map = {
        'created': 'created',
        'id': 'id',
        'new_version': 'new_version',
        'org_id': 'org_id',
        'revision_number': 'revision_number',
        'services': 'services',
        'title': 'title',
        'updated': 'updated',
        'version': 'version'
    }

    def __init__(self, created=None, id=None, new_version=None, org_id=None, revision_number=None, services=None, title=None, updated=None, version=None):  # noqa: E501
        """Stack - a model defined in Swagger"""  # noqa: E501

        self._created = None
        self._id = None
        self._new_version = None
        self._org_id = None
        self._revision_number = None
        self._services = None
        self._title = None
        self._updated = None
        self._version = None
        self.discriminator = None

        self.created = created
        self.id = id
        if new_version is not None:
            self.new_version = new_version
        self.org_id = org_id
        if revision_number is not None:
            self.revision_number = revision_number
        self.services = services
        self.title = title
        self.updated = updated
        if version is not None:
            self.version = version

    @property
    def created(self):
        """Gets the created of this Stack.  # noqa: E501


        :return: The created of this Stack.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Stack.


        :param created: The created of this Stack.  # noqa: E501
        :type: int
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def id(self):
        """Gets the id of this Stack.  # noqa: E501


        :return: The id of this Stack.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Stack.


        :param id: The id of this Stack.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def new_version(self):
        """Gets the new_version of this Stack.  # noqa: E501


        :return: The new_version of this Stack.  # noqa: E501
        :rtype: str
        """
        return self._new_version

    @new_version.setter
    def new_version(self, new_version):
        """Sets the new_version of this Stack.


        :param new_version: The new_version of this Stack.  # noqa: E501
        :type: str
        """

        self._new_version = new_version

    @property
    def org_id(self):
        """Gets the org_id of this Stack.  # noqa: E501


        :return: The org_id of this Stack.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this Stack.


        :param org_id: The org_id of this Stack.  # noqa: E501
        :type: str
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def revision_number(self):
        """Gets the revision_number of this Stack.  # noqa: E501


        :return: The revision_number of this Stack.  # noqa: E501
        :rtype: int
        """
        return self._revision_number

    @revision_number.setter
    def revision_number(self, revision_number):
        """Sets the revision_number of this Stack.


        :param revision_number: The revision_number of this Stack.  # noqa: E501
        :type: int
        """

        self._revision_number = revision_number

    @property
    def services(self):
        """Gets the services of this Stack.  # noqa: E501


        :return: The services of this Stack.  # noqa: E501
        :rtype: list[StackService]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this Stack.


        :param services: The services of this Stack.  # noqa: E501
        :type: list[StackService]
        """
        if services is None:
            raise ValueError("Invalid value for `services`, must not be `None`")  # noqa: E501

        self._services = services

    @property
    def title(self):
        """Gets the title of this Stack.  # noqa: E501


        :return: The title of this Stack.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Stack.


        :param title: The title of this Stack.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def updated(self):
        """Gets the updated of this Stack.  # noqa: E501


        :return: The updated of this Stack.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Stack.


        :param updated: The updated of this Stack.  # noqa: E501
        :type: int
        """
        if updated is None:
            raise ValueError("Invalid value for `updated`, must not be `None`")  # noqa: E501

        self._updated = updated

    @property
    def version(self):
        """Gets the version of this Stack.  # noqa: E501


        :return: The version of this Stack.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Stack.


        :param version: The version of this Stack.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(Stack, dict):
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
        if not isinstance(other, Stack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
