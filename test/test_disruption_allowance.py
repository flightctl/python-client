# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flightctl.models.disruption_allowance import DisruptionAllowance

class TestDisruptionAllowance(unittest.TestCase):
    """DisruptionAllowance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DisruptionAllowance:
        """Test DisruptionAllowance
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DisruptionAllowance`
        """
        model = DisruptionAllowance()
        if include_optional:
            return DisruptionAllowance(
                group_by = [
                    ''
                    ],
                min_available = 56,
                max_unavailable = 56
            )
        else:
            return DisruptionAllowance(
        )
        """

    def testDisruptionAllowance(self):
        """Test DisruptionAllowance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
