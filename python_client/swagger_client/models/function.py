# coding: utf-8

"""
    faasnap

    FaaSnap API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Function(object):
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
        'func_name': 'str',
        'image': 'str',
        'kernel': 'str',
        'vcpu': 'int',
        'mem_size': 'int'
    }

    attribute_map = {
        'func_name': 'func_name',
        'image': 'image',
        'kernel': 'kernel',
        'vcpu': 'vcpu',
        'mem_size': 'mem_size'
    }

    def __init__(self, func_name=None, image=None, kernel=None, vcpu=None, mem_size=None, _configuration=None):  # noqa: E501
        """Function - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._func_name = None
        self._image = None
        self._kernel = None
        self._vcpu = None
        self._mem_size = None
        self.discriminator = None

        self.func_name = func_name
        if image is not None:
            self.image = image
        if kernel is not None:
            self.kernel = kernel
        if vcpu is not None:
            self.vcpu = vcpu
        if mem_size is not None:
            self.mem_size = mem_size

    @property
    def func_name(self):
        """Gets the func_name of this Function.  # noqa: E501


        :return: The func_name of this Function.  # noqa: E501
        :rtype: str
        """
        return self._func_name

    @func_name.setter
    def func_name(self, func_name):
        """Sets the func_name of this Function.


        :param func_name: The func_name of this Function.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and func_name is None:
            raise ValueError("Invalid value for `func_name`, must not be `None`")  # noqa: E501

        self._func_name = func_name

    @property
    def image(self):
        """Gets the image of this Function.  # noqa: E501


        :return: The image of this Function.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Function.


        :param image: The image of this Function.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def kernel(self):
        """Gets the kernel of this Function.  # noqa: E501


        :return: The kernel of this Function.  # noqa: E501
        :rtype: str
        """
        return self._kernel

    @kernel.setter
    def kernel(self, kernel):
        """Sets the kernel of this Function.


        :param kernel: The kernel of this Function.  # noqa: E501
        :type: str
        """

        self._kernel = kernel

    @property
    def vcpu(self):
        """Gets the vcpu of this Function.  # noqa: E501


        :return: The vcpu of this Function.  # noqa: E501
        :rtype: int
        """
        return self._vcpu

    @vcpu.setter
    def vcpu(self, vcpu):
        """Sets the vcpu of this Function.


        :param vcpu: The vcpu of this Function.  # noqa: E501
        :type: int
        """

        self._vcpu = vcpu

    @property
    def mem_size(self):
        """Gets the mem_size of this Function.  # noqa: E501


        :return: The mem_size of this Function.  # noqa: E501
        :rtype: int
        """
        return self._mem_size

    @mem_size.setter
    def mem_size(self, mem_size):
        """Sets the mem_size of this Function.


        :param mem_size: The mem_size of this Function.  # noqa: E501
        :type: int
        """

        self._mem_size = mem_size

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
        if issubclass(Function, dict):
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
        if not isinstance(other, Function):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Function):
            return True

        return self.to_dict() != other.to_dict()
