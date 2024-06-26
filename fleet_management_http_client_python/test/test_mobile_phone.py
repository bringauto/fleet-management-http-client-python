# coding: utf-8

"""
    BringAuto Fleet Management v2 API

    Specification for BringAuto fleet backend HTTP API

    The version of the OpenAPI document: 1.3.0
    Contact: fleet@bringauto.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fleet_management_http_client_python.models.mobile_phone import MobilePhone

class TestMobilePhone(unittest.TestCase):
    """MobilePhone unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MobilePhone:
        """Test MobilePhone
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MobilePhone`
        """
        model = MobilePhone()
        if include_optional:
            return MobilePhone(
                phone = '+420123456789'
            )
        else:
            return MobilePhone(
        )
        """

    def testMobilePhone(self):
        """Test MobilePhone"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
