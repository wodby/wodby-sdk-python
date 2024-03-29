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

from wodby.models.request_instance_create_git import RequestInstanceCreateGit  # noqa: F401,E501


class RequestInstanceDeployCodebase(object):
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
        'git': 'RequestInstanceCreateGit',
        'post_deployment': 'bool'
    }

    attribute_map = {
        'git': 'git',
        'post_deployment': 'post_deployment'
    }

    def __init__(self, git=None, post_deployment=None):  # noqa: E501
        """RequestInstanceDeployCodebase - a model defined in Swagger"""  # noqa: E501

        self._git = None
        self._post_deployment = None
        self.discriminator = None

        if git is not None:
            self.git = git
        if post_deployment is not None:
            self.post_deployment = post_deployment

    @property
    def git(self):
        """Gets the git of this RequestInstanceDeployCodebase.  # noqa: E501


        :return: The git of this RequestInstanceDeployCodebase.  # noqa: E501
        :rtype: RequestInstanceCreateGit
        """
        return self._git

    @git.setter
    def git(self, git):
        """Sets the git of this RequestInstanceDeployCodebase.


        :param git: The git of this RequestInstanceDeployCodebase.  # noqa: E501
        :type: RequestInstanceCreateGit
        """

        self._git = git

    @property
    def post_deployment(self):
        """Gets the post_deployment of this RequestInstanceDeployCodebase.  # noqa: E501


        :return: The post_deployment of this RequestInstanceDeployCodebase.  # noqa: E501
        :rtype: bool
        """
        return self._post_deployment

    @post_deployment.setter
    def post_deployment(self, post_deployment):
        """Sets the post_deployment of this RequestInstanceDeployCodebase.


        :param post_deployment: The post_deployment of this RequestInstanceDeployCodebase.  # noqa: E501
        :type: bool
        """

        self._post_deployment = post_deployment

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
        if issubclass(RequestInstanceDeployCodebase, dict):
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
        if not isinstance(other, RequestInstanceDeployCodebase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
