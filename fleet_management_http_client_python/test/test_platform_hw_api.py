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

from fleet_management_http_client_python.api.platform_hw_api import PlatformHWApi


class TestPlatformHWApi(unittest.TestCase):
    """PlatformHWApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PlatformHWApi()

    def tearDown(self) -> None:
        pass

    def test_create_hw(self) -> None:
        """Test case for create_hw

        Create a new Platform HW object.
        """
        pass

    def test_delete_hw(self) -> None:
        """Test case for delete_hw

        Delete Platform HW with given ID.
        """
        pass

    def test_get_hw(self) -> None:
        """Test case for get_hw

        Find Platform HW with given ID.
        """
        pass

    def test_get_hws(self) -> None:
        """Test case for get_hws

        Find and return all existing Platform HW.
        """
        pass


if __name__ == '__main__':
    unittest.main()