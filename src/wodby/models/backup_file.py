# coding: utf-8

"""
    Wodby API Client

    Wodby Developer Documentation https://wodby.com/docs/dev  # noqa: E501

    OpenAPI spec version: 3.0.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BackupFile(object):
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
        'mirrored_url': 'str',
        'name': 'str',
        'spent': 'int',
        'status': 'str',
        'updated': 'int',
        'url': 'str'
    }

    attribute_map = {
        'created': 'created',
        'mirrored_url': 'mirrored_url',
        'name': 'name',
        'spent': 'spent',
        'status': 'status',
        'updated': 'updated',
        'url': 'url'
    }

    def __init__(self, created=None, mirrored_url=None, name=None, spent=None, status=None, updated=None, url=None):  # noqa: E501
        """BackupFile - a model defined in Swagger"""  # noqa: E501

        self._created = None
        self._mirrored_url = None
        self._name = None
        self._spent = None
        self._status = None
        self._updated = None
        self._url = None
        self.discriminator = None

        self.created = created
        if mirrored_url is not None:
            self.mirrored_url = mirrored_url
        self.name = name
        if spent is not None:
            self.spent = spent
        self.status = status
        self.updated = updated
        if url is not None:
            self.url = url

    @property
    def created(self):
        """Gets the created of this BackupFile.  # noqa: E501


        :return: The created of this BackupFile.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this BackupFile.


        :param created: The created of this BackupFile.  # noqa: E501
        :type: int
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def mirrored_url(self):
        """Gets the mirrored_url of this BackupFile.  # noqa: E501


        :return: The mirrored_url of this BackupFile.  # noqa: E501
        :rtype: str
        """
        return self._mirrored_url

    @mirrored_url.setter
    def mirrored_url(self, mirrored_url):
        """Sets the mirrored_url of this BackupFile.


        :param mirrored_url: The mirrored_url of this BackupFile.  # noqa: E501
        :type: str
        """

        self._mirrored_url = mirrored_url

    @property
    def name(self):
        """Gets the name of this BackupFile.  # noqa: E501


        :return: The name of this BackupFile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BackupFile.


        :param name: The name of this BackupFile.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        allowed_values = ["database", "files"]  # noqa: E501
        if name not in allowed_values:
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"  # noqa: E501
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def spent(self):
        """Gets the spent of this BackupFile.  # noqa: E501


        :return: The spent of this BackupFile.  # noqa: E501
        :rtype: int
        """
        return self._spent

    @spent.setter
    def spent(self, spent):
        """Sets the spent of this BackupFile.


        :param spent: The spent of this BackupFile.  # noqa: E501
        :type: int
        """

        self._spent = spent

    @property
    def status(self):
        """Gets the status of this BackupFile.  # noqa: E501


        :return: The status of this BackupFile.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BackupFile.


        :param status: The status of this BackupFile.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["ok", "error", "waiting", "creating", "restoring", "deleting"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def updated(self):
        """Gets the updated of this BackupFile.  # noqa: E501


        :return: The updated of this BackupFile.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this BackupFile.


        :param updated: The updated of this BackupFile.  # noqa: E501
        :type: int
        """
        if updated is None:
            raise ValueError("Invalid value for `updated`, must not be `None`")  # noqa: E501

        self._updated = updated

    @property
    def url(self):
        """Gets the url of this BackupFile.  # noqa: E501


        :return: The url of this BackupFile.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this BackupFile.


        :param url: The url of this BackupFile.  # noqa: E501
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
        if issubclass(BackupFile, dict):
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
        if not isinstance(other, BackupFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
