# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.certificate_signing_request_spec import CertificateSigningRequestSpec

class TestCertificateSigningRequestSpec(unittest.TestCase):
    """CertificateSigningRequestSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificateSigningRequestSpec:
        """Test CertificateSigningRequestSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificateSigningRequestSpec`
        """
        model = CertificateSigningRequestSpec()
        if include_optional:
            return CertificateSigningRequestSpec(
                expiration_seconds = 56,
                extra = {
                    'key' : [
                        ''
                        ]
                    },
                request = 'YQ==',
                signer_name = '',
                uid = '',
                usages = [
                    ''
                    ],
                username = ''
            )
        else:
            return CertificateSigningRequestSpec(
                signer_name = '',
        )
        """

    def testCertificateSigningRequestSpec(self):
        """Test CertificateSigningRequestSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()