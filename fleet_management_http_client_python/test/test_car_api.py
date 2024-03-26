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

from fleet_management_http_client_python.api.car_api import CarApi


class TestCarApi(unittest.TestCase):
    """CarApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CarApi()

    def tearDown(self) -> None:
        pass

    def test_create_car(self) -> None:
        """Test case for create_car

        Create a new Car object.
        """
        pass

    def test_delete_car(self) -> None:
        """Test case for delete_car

        Delete a Car identified by its ID.
        """
        pass

    def test_get_car(self) -> None:
        """Test case for get_car

        Find a single Car by its ID.
        """
        pass

    def test_get_cars(self) -> None:
        """Test case for get_cars

        Find and return all existing Cars.
        """
        pass

    def test_update_car(self) -> None:
        """Test case for update_car

        Update already existing Car.
        """
        pass


if __name__ == '__main__':
    unittest.main()