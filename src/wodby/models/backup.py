# coding: utf-8

"""
    Wodby API Client

    Wodby Developer Documentation https://wodby.com/docs/dev  # noqa: E501

    OpenAPI spec version: 3.0.16
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wodby.models.backup_files import BackupFiles  # noqa: F401,E501


class Backup(object):
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
        'files': 'BackupFiles',
        'id': 'str',
        'instance_id': 'str',
        'org_id': 'str',
        'spent': 'int',
        'status': 'str',
        'type': 'str',
        'updated': 'int'
    }

    attribute_map = {
        'created': 'created',
        'files': 'files',
        'id': 'id',
        'instance_id': 'instance_id',
        'org_id': 'org_id',
        'spent': 'spent',
        'status': 'status',
        'type': 'type',
        'updated': 'updated'
    }

    def __init__(self, created=None, files=None, id=None, instance_id=None, org_id=None, spent=None, status=None, type=None, updated=None):  # noqa: E501
        """Backup - a model defined in Swagger"""  # noqa: E501

        self._created = None
        self._files = None
        self._id = None
        self._instance_id = None
        self._org_id = None
        self._spent = None
        self._status = None
        self._type = None
        self._updated = None
        self.discriminator = None

        self.created = created
        if files is not None:
            self.files = files
        self.id = id
        self.instance_id = instance_id
        self.org_id = org_id
        if spent is not None:
            self.spent = spent
        self.status = status
        self.type = type
        self.updated = updated

    @property
    def created(self):
        """Gets the created of this Backup.  # noqa: E501


        :return: The created of this Backup.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Backup.


        :param created: The created of this Backup.  # noqa: E501
        :type: int
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def files(self):
        """Gets the files of this Backup.  # noqa: E501


        :return: The files of this Backup.  # noqa: E501
        :rtype: BackupFiles
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Backup.


        :param files: The files of this Backup.  # noqa: E501
        :type: BackupFiles
        """

        self._files = files

    @property
    def id(self):
        """Gets the id of this Backup.  # noqa: E501


        :return: The id of this Backup.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Backup.


        :param id: The id of this Backup.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def instance_id(self):
        """Gets the instance_id of this Backup.  # noqa: E501


        :return: The instance_id of this Backup.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this Backup.


        :param instance_id: The instance_id of this Backup.  # noqa: E501
        :type: str
        """
        if instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def org_id(self):
        """Gets the org_id of this Backup.  # noqa: E501


        :return: The org_id of this Backup.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this Backup.


        :param org_id: The org_id of this Backup.  # noqa: E501
        :type: str
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def spent(self):
        """Gets the spent of this Backup.  # noqa: E501


        :return: The spent of this Backup.  # noqa: E501
        :rtype: int
        """
        return self._spent

    @spent.setter
    def spent(self, spent):
        """Sets the spent of this Backup.


        :param spent: The spent of this Backup.  # noqa: E501
        :type: int
        """

        self._spent = spent

    @property
    def status(self):
        """Gets the status of this Backup.  # noqa: E501


        :return: The status of this Backup.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Backup.


        :param status: The status of this Backup.  # noqa: E501
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
    def type(self):
        """Gets the type of this Backup.  # noqa: E501


        :return: The type of this Backup.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Backup.


        :param type: The type of this Backup.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["system", "daily", "manual"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def updated(self):
        """Gets the updated of this Backup.  # noqa: E501


        :return: The updated of this Backup.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Backup.


        :param updated: The updated of this Backup.  # noqa: E501
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
        if issubclass(Backup, dict):
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
        if not isinstance(other, Backup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
