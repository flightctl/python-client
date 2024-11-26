# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flightctl.models.repository_status import RepositoryStatus

class TestRepositoryStatus(unittest.TestCase):
    """RepositoryStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RepositoryStatus:
        """Test RepositoryStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepositoryStatus`
        """
        model = RepositoryStatus()
        if include_optional:
            return RepositoryStatus(
                conditions = [
                    flightctl.models.condition.Condition(
                        type = 'Approved', 
                        status = 'True', 
                        observed_generation = 56, 
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        reason = '', )
                    ]
            )
        else:
            return RepositoryStatus(
                conditions = [
                    flightctl.models.condition.Condition(
                        type = 'Approved', 
                        status = 'True', 
                        observed_generation = 56, 
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        reason = '', )
                    ],
        )
        """

    def testRepositoryStatus(self):
        """Test RepositoryStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
