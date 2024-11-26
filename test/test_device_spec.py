# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flightctl.models.device_spec import DeviceSpec

class TestDeviceSpec(unittest.TestCase):
    """DeviceSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceSpec:
        """Test DeviceSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceSpec`
        """
        model = DeviceSpec()
        if include_optional:
            return DeviceSpec(
                os = flightctl.models.device_os_spec.DeviceOSSpec(
                    image = '', ),
                config = [
                    null
                    ],
                hooks = flightctl.models.device_hooks_spec.DeviceHooksSpec(
                    before_updating = [
                        flightctl.models.device_update_hook_spec.DeviceUpdateHookSpec(
                            name = '', 
                            description = '', 
                            actions = [
                                flightctl.models.hook_action.HookAction()
                                ], 
                            on_file = [
                                'Create'
                                ], 
                            path = '', )
                        ], 
                    after_updating = [
                        flightctl.models.device_update_hook_spec.DeviceUpdateHookSpec(
                            name = '', 
                            description = '', 
                            actions = [
                                flightctl.models.hook_action.HookAction()
                                ], 
                            path = '', )
                        ], 
                    before_rebooting = [
                        flightctl.models.device_reboot_hook_spec.DeviceRebootHookSpec(
                            name = '', 
                            description = '', 
                            actions = [
                                flightctl.models.hook_action.HookAction()
                                ], )
                        ], 
                    after_rebooting = [
                        flightctl.models.device_reboot_hook_spec.DeviceRebootHookSpec(
                            name = '', 
                            description = '', 
                            actions = [
                                flightctl.models.hook_action.HookAction()
                                ], )
                        ], ),
                applications = [
                    flightctl.models.application_spec.ApplicationSpec()
                    ],
                systemd = flightctl.models.device_spec_systemd.DeviceSpec_systemd(
                    match_patterns = [
                        'ge34w9Wa*CLfoo\\yJX2gCb'
                        ], ),
                resources = [
                    null
                    ]
            )
        else:
            return DeviceSpec(
        )
        """

    def testDeviceSpec(self):
        """Test DeviceSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
