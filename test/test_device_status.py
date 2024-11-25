# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.device_status import DeviceStatus

class TestDeviceStatus(unittest.TestCase):
    """DeviceStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceStatus:
        """Test DeviceStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceStatus`
        """
        model = DeviceStatus()
        if include_optional:
            return DeviceStatus(
                conditions = [
                    openapi_client.models.condition.Condition(
                        type = 'Approved', 
                        status = 'True', 
                        observed_generation = 56, 
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        reason = '', )
                    ],
                system_info = openapi_client.models.device_system_info.DeviceSystemInfo(
                    architecture = '', 
                    boot_id = '', 
                    operating_system = '', ),
                applications = [
                    openapi_client.models.device_application_status.DeviceApplicationStatus(
                        name = '', 
                        ready = '', 
                        restarts = 56, 
                        status = 'Preparing', )
                    ],
                applications_summary = openapi_client.models.device_applications_summary_status.DeviceApplicationsSummaryStatus(
                    status = 'Healthy', 
                    info = '', ),
                resources = openapi_client.models.device_resource_status.DeviceResourceStatus(
                    cpu = 'Healthy', 
                    memory = 'Healthy', 
                    disk = 'Healthy', ),
                integrity = openapi_client.models.device_integrity_status.DeviceIntegrityStatus(
                    summary = openapi_client.models.device_integrity_status_summary.DeviceIntegrityStatusSummary(
                        status = 'Passed', 
                        info = '', ), ),
                config = openapi_client.models.device_config_status.DeviceConfigStatus(
                    rendered_version = '', ),
                os = openapi_client.models.device_os_status.DeviceOSStatus(
                    image = '', 
                    image_digest = '', ),
                updated = openapi_client.models.device_updated_status.DeviceUpdatedStatus(
                    status = 'UpToDate', 
                    info = '', ),
                summary = openapi_client.models.device_summary_status.DeviceSummaryStatus(
                    status = 'Online', 
                    info = '', ),
                last_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return DeviceStatus(
                conditions = [
                    openapi_client.models.condition.Condition(
                        type = 'Approved', 
                        status = 'True', 
                        observed_generation = 56, 
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        reason = '', )
                    ],
                system_info = openapi_client.models.device_system_info.DeviceSystemInfo(
                    architecture = '', 
                    boot_id = '', 
                    operating_system = '', ),
                applications = [
                    openapi_client.models.device_application_status.DeviceApplicationStatus(
                        name = '', 
                        ready = '', 
                        restarts = 56, 
                        status = 'Preparing', )
                    ],
                applications_summary = openapi_client.models.device_applications_summary_status.DeviceApplicationsSummaryStatus(
                    status = 'Healthy', 
                    info = '', ),
                resources = openapi_client.models.device_resource_status.DeviceResourceStatus(
                    cpu = 'Healthy', 
                    memory = 'Healthy', 
                    disk = 'Healthy', ),
                integrity = openapi_client.models.device_integrity_status.DeviceIntegrityStatus(
                    summary = openapi_client.models.device_integrity_status_summary.DeviceIntegrityStatusSummary(
                        status = 'Passed', 
                        info = '', ), ),
                config = openapi_client.models.device_config_status.DeviceConfigStatus(
                    rendered_version = '', ),
                os = openapi_client.models.device_os_status.DeviceOSStatus(
                    image = '', 
                    image_digest = '', ),
                updated = openapi_client.models.device_updated_status.DeviceUpdatedStatus(
                    status = 'UpToDate', 
                    info = '', ),
                summary = openapi_client.models.device_summary_status.DeviceSummaryStatus(
                    status = 'Online', 
                    info = '', ),
                last_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testDeviceStatus(self):
        """Test DeviceStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()