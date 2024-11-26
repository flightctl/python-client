# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flightctl.models.device_system_info import DeviceSystemInfo

class TestDeviceSystemInfo(unittest.TestCase):
    """DeviceSystemInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceSystemInfo:
        """Test DeviceSystemInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceSystemInfo`
        """
        model = DeviceSystemInfo()
        if include_optional:
            return DeviceSystemInfo(
                architecture = '',
                boot_id = '',
                operating_system = ''
            )
        else:
            return DeviceSystemInfo(
                architecture = '',
                boot_id = '',
                operating_system = '',
        )
        """

    def testDeviceSystemInfo(self):
        """Test DeviceSystemInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
