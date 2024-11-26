# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flightctl.models.device_reboot_hook_spec import DeviceRebootHookSpec

class TestDeviceRebootHookSpec(unittest.TestCase):
    """DeviceRebootHookSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceRebootHookSpec:
        """Test DeviceRebootHookSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceRebootHookSpec`
        """
        model = DeviceRebootHookSpec()
        if include_optional:
            return DeviceRebootHookSpec(
                name = '',
                description = '',
                actions = [
                    flightctl.models.hook_action.HookAction()
                    ]
            )
        else:
            return DeviceRebootHookSpec(
                actions = [
                    flightctl.models.hook_action.HookAction()
                    ],
        )
        """

    def testDeviceRebootHookSpec(self):
        """Test DeviceRebootHookSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
