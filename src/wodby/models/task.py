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


class Task(object):
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
        'end': 'int',
        'id': 'str',
        'org_id': 'str',
        'start': 'int',
        'status': 'str',
        'title': 'str',
        'ttl': 'int',
        'updated': 'int'
    }

    attribute_map = {
        'created': 'created',
        'end': 'end',
        'id': 'id',
        'org_id': 'org_id',
        'start': 'start',
        'status': 'status',
        'title': 'title',
        'ttl': 'ttl',
        'updated': 'updated'
    }

    def __init__(self, created=None, end=None, id=None, org_id=None, start=None, status=None, title=None, ttl=None, updated=None):  # noqa: E501
        """Task - a model defined in Swagger"""  # noqa: E501

        self._created = None
        self._end = None
        self._id = None
        self._org_id = None
        self._start = None
        self._status = None
        self._title = None
        self._ttl = None
        self._updated = None
        self.discriminator = None

        self.created = created
        if end is not None:
            self.end = end
        self.id = id
        self.org_id = org_id
        if start is not None:
            self.start = start
        self.status = status
        self.title = title
        self.ttl = ttl
        self.updated = updated

    @property
    def created(self):
        """Gets the created of this Task.  # noqa: E501


        :return: The created of this Task.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Task.


        :param created: The created of this Task.  # noqa: E501
        :type: int
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def end(self):
        """Gets the end of this Task.  # noqa: E501


        :return: The end of this Task.  # noqa: E501
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this Task.


        :param end: The end of this Task.  # noqa: E501
        :type: int
        """

        self._end = end

    @property
    def id(self):
        """Gets the id of this Task.  # noqa: E501


        :return: The id of this Task.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Task.


        :param id: The id of this Task.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def org_id(self):
        """Gets the org_id of this Task.  # noqa: E501


        :return: The org_id of this Task.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this Task.


        :param org_id: The org_id of this Task.  # noqa: E501
        :type: str
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def start(self):
        """Gets the start of this Task.  # noqa: E501


        :return: The start of this Task.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this Task.


        :param start: The start of this Task.  # noqa: E501
        :type: int
        """

        self._start = start

    @property
    def status(self):
        """Gets the status of this Task.  # noqa: E501


        :return: The status of this Task.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Task.


        :param status: The status of this Task.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["waiting", "in_progress", "done", "failed", "canceled"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def title(self):
        """Gets the title of this Task.  # noqa: E501


        :return: The title of this Task.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Task.


        :param title: The title of this Task.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def ttl(self):
        """Gets the ttl of this Task.  # noqa: E501


        :return: The ttl of this Task.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this Task.


        :param ttl: The ttl of this Task.  # noqa: E501
        :type: int
        """
        if ttl is None:
            raise ValueError("Invalid value for `ttl`, must not be `None`")  # noqa: E501

        self._ttl = ttl

    @property
    def updated(self):
        """Gets the updated of this Task.  # noqa: E501


        :return: The updated of this Task.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Task.


        :param updated: The updated of this Task.  # noqa: E501
        :type: int
        """
        if updated is None:
            raise ValueError("Invalid value for `updated`, must not be `None`")  # noqa: E501

        self._updated = updated

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
        if issubclass(Task, dict):
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
        if not isinstance(other, Task):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
