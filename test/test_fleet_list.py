# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.fleet_list import FleetList

class TestFleetList(unittest.TestCase):
    """FleetList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FleetList:
        """Test FleetList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FleetList`
        """
        model = FleetList()
        if include_optional:
            return FleetList(
                api_version = '',
                kind = '',
                metadata = openapi_client.models.list_meta.ListMeta(
                    continue = '', 
                    remaining_item_count = 56, ),
                items = [
                    openapi_client.models.fleet.Fleet(
                        api_version = '', 
                        kind = '', 
                        metadata = openapi_client.models.object_meta.ObjectMeta(
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            name = '', 
                            labels = {
                                'key' : ''
                                }, 
                            generation = 56, 
                            owner = '', 
                            annotations = {
                                'key' : ''
                                }, 
                            resource_version = '', ), 
                        spec = openapi_client.models.fleet_spec.FleetSpec(
                            selector = openapi_client.models.label_selector.LabelSelector(
                                match_labels = {
                                    'key' : ''
                                    }, 
                                match_expressions = [
                                    openapi_client.models.match_expression.MatchExpression(
                                        key = '', 
                                        operator = 'In', 
                                        values = [
                                            ''
                                            ], )
                                    ], ), 
                            rollout_policy = openapi_client.models.rollout_policy.RolloutPolicy(
                                disruption_allowance = openapi_client.models.disruption_allowance.DisruptionAllowance(
                                    group_by = [
                                        ''
                                        ], 
                                    min_available = 56, 
                                    max_unavailable = 56, ), 
                                device_selection = openapi_client.models.rollout_device_selection.RolloutDeviceSelection(
                                    strategy = '', ), 
                                success_threshold = '', 
                                default_update_timeout = '68072888001528021798096225500h', ), 
                            template = openapi_client.models.fleet_spec_template.FleetSpec_template(
                                spec = openapi_client.models.device_spec.DeviceSpec(
                                    os = openapi_client.models.device_os_spec.DeviceOSSpec(
                                        image = '', ), 
                                    config = [
                                        null
                                        ], 
                                    hooks = openapi_client.models.device_hooks_spec.DeviceHooksSpec(
                                        before_updating = [
                                            openapi_client.models.device_update_hook_spec.DeviceUpdateHookSpec(
                                                name = '', 
                                                description = '', 
                                                actions = [
                                                    openapi_client.models.hook_action.HookAction()
                                                    ], 
                                                on_file = [
                                                    'Create'
                                                    ], 
                                                path = '', )
                                            ], 
                                        after_updating = [
                                            openapi_client.models.device_update_hook_spec.DeviceUpdateHookSpec(
                                                name = '', 
                                                description = '', 
                                                actions = [
                                                    openapi_client.models.hook_action.HookAction()
                                                    ], 
                                                path = '', )
                                            ], 
                                        before_rebooting = [
                                            openapi_client.models.device_reboot_hook_spec.DeviceRebootHookSpec(
                                                name = '', 
                                                description = '', 
                                                actions = [
                                                    openapi_client.models.hook_action.HookAction()
                                                    ], )
                                            ], 
                                        after_rebooting = [
                                            openapi_client.models.device_reboot_hook_spec.DeviceRebootHookSpec(
                                                name = '', 
                                                description = '', 
                                                actions = [
                                                    openapi_client.models.hook_action.HookAction()
                                                    ], )
                                            ], ), 
                                    applications = [
                                        openapi_client.models.application_spec.ApplicationSpec()
                                        ], 
                                    systemd = openapi_client.models.device_spec_systemd.DeviceSpec_systemd(
                                        match_patterns = [
                                            'ge34w9Wa*CLfoo\\yJX2gCb'
                                            ], ), 
                                    resources = [
                                        null
                                        ], ), ), ), 
                        status = openapi_client.models.fleet_status.FleetStatus(
                            rollout = openapi_client.models.fleet_rollout_status.FleetRolloutStatus(
                                current_batch = 56, ), 
                            conditions = [
                                openapi_client.models.condition.Condition(
                                    type = 'Approved', 
                                    status = 'True', 
                                    observed_generation = 56, 
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '', 
                                    reason = '', )
                                ], 
                            devices_summary = openapi_client.models.devices_summary.DevicesSummary(
                                total = 56, 
                                application_status = {
                                    'key' : 56
                                    }, 
                                summary_status = {
                                    'key' : 56
                                    }, 
                                update_status = {
                                    'key' : 56
                                    }, ), ), )
                    ]
            )
        else:
            return FleetList(
                api_version = '',
                kind = '',
                metadata = openapi_client.models.list_meta.ListMeta(
                    continue = '', 
                    remaining_item_count = 56, ),
                items = [
                    openapi_client.models.fleet.Fleet(
                        api_version = '', 
                        kind = '', 
                        metadata = openapi_client.models.object_meta.ObjectMeta(
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            name = '', 
                            labels = {
                                'key' : ''
                                }, 
                            generation = 56, 
                            owner = '', 
                            annotations = {
                                'key' : ''
                                }, 
                            resource_version = '', ), 
                        spec = openapi_client.models.fleet_spec.FleetSpec(
                            selector = openapi_client.models.label_selector.LabelSelector(
                                match_labels = {
                                    'key' : ''
                                    }, 
                                match_expressions = [
                                    openapi_client.models.match_expression.MatchExpression(
                                        key = '', 
                                        operator = 'In', 
                                        values = [
                                            ''
                                            ], )
                                    ], ), 
                            rollout_policy = openapi_client.models.rollout_policy.RolloutPolicy(
                                disruption_allowance = openapi_client.models.disruption_allowance.DisruptionAllowance(
                                    group_by = [
                                        ''
                                        ], 
                                    min_available = 56, 
                                    max_unavailable = 56, ), 
                                device_selection = openapi_client.models.rollout_device_selection.RolloutDeviceSelection(
                                    strategy = '', ), 
                                success_threshold = '', 
                                default_update_timeout = '68072888001528021798096225500h', ), 
                            template = openapi_client.models.fleet_spec_template.FleetSpec_template(
                                spec = openapi_client.models.device_spec.DeviceSpec(
                                    os = openapi_client.models.device_os_spec.DeviceOSSpec(
                                        image = '', ), 
                                    config = [
                                        null
                                        ], 
                                    hooks = openapi_client.models.device_hooks_spec.DeviceHooksSpec(
                                        before_updating = [
                                            openapi_client.models.device_update_hook_spec.DeviceUpdateHookSpec(
                                                name = '', 
                                                description = '', 
                                                actions = [
                                                    openapi_client.models.hook_action.HookAction()
                                                    ], 
                                                on_file = [
                                                    'Create'
                                                    ], 
                                                path = '', )
                                            ], 
                                        after_updating = [
                                            openapi_client.models.device_update_hook_spec.DeviceUpdateHookSpec(
                                                name = '', 
                                                description = '', 
                                                actions = [
                                                    openapi_client.models.hook_action.HookAction()
                                                    ], 
                                                path = '', )
                                            ], 
                                        before_rebooting = [
                                            openapi_client.models.device_reboot_hook_spec.DeviceRebootHookSpec(
                                                name = '', 
                                                description = '', 
                                                actions = [
                                                    openapi_client.models.hook_action.HookAction()
                                                    ], )
                                            ], 
                                        after_rebooting = [
                                            openapi_client.models.device_reboot_hook_spec.DeviceRebootHookSpec(
                                                name = '', 
                                                description = '', 
                                                actions = [
                                                    openapi_client.models.hook_action.HookAction()
                                                    ], )
                                            ], ), 
                                    applications = [
                                        openapi_client.models.application_spec.ApplicationSpec()
                                        ], 
                                    systemd = openapi_client.models.device_spec_systemd.DeviceSpec_systemd(
                                        match_patterns = [
                                            'ge34w9Wa*CLfoo\\yJX2gCb'
                                            ], ), 
                                    resources = [
                                        null
                                        ], ), ), ), 
                        status = openapi_client.models.fleet_status.FleetStatus(
                            rollout = openapi_client.models.fleet_rollout_status.FleetRolloutStatus(
                                current_batch = 56, ), 
                            conditions = [
                                openapi_client.models.condition.Condition(
                                    type = 'Approved', 
                                    status = 'True', 
                                    observed_generation = 56, 
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '', 
                                    reason = '', )
                                ], 
                            devices_summary = openapi_client.models.devices_summary.DevicesSummary(
                                total = 56, 
                                application_status = {
                                    'key' : 56
                                    }, 
                                summary_status = {
                                    'key' : 56
                                    }, 
                                update_status = {
                                    'key' : 56
                                    }, ), ), )
                    ],
        )
        """

    def testFleetList(self):
        """Test FleetList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()