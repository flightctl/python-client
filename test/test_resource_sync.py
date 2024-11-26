# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flightctl.models.resource_sync import ResourceSync

class TestResourceSync(unittest.TestCase):
    """ResourceSync unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceSync:
        """Test ResourceSync
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceSync`
        """
        model = ResourceSync()
        if include_optional:
            return ResourceSync(
                api_version = '',
                kind = '',
                metadata = flightctl.models.object_meta.ObjectMeta(
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
                spec = flightctl.models.resource_sync_spec.ResourceSyncSpec(
                    repository = '', 
                    target_revision = '', 
                    path = '', ),
                status = flightctl.models.resource_sync_status.ResourceSyncStatus(
                    observed_commit = '', 
                    observed_generation = 56, 
                    conditions = [
                        flightctl.models.condition.Condition(
                            type = 'Approved', 
                            status = 'True', 
                            observed_generation = 56, 
                            last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            message = '', 
                            reason = '', )
                        ], )
            )
        else:
            return ResourceSync(
                api_version = '',
                kind = '',
                metadata = flightctl.models.object_meta.ObjectMeta(
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
                spec = flightctl.models.resource_sync_spec.ResourceSyncSpec(
                    repository = '', 
                    target_revision = '', 
                    path = '', ),
        )
        """

    def testResourceSync(self):
        """Test ResourceSync"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
