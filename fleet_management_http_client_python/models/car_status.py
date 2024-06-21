# coding: utf-8

"""
    BringAuto Fleet Management v2 API

    Specification for BringAuto fleet backend HTTP API

    The version of the OpenAPI document: 3.1.6
    Contact: fleet@bringauto.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class CarStatus(str, Enum):
    """
    Car Status enum
    """

    """
    allowed enum values
    """
    IDLE = 'idle'
    CHARGING = 'charging'
    OUT_OF_ORDER = 'out_of_order'
    DRIVING = 'driving'
    IN_STOP = 'in_stop'
    PAUSED_BY_PHONE = 'paused_by_phone'
    PAUSED_BY_OBSTACLE = 'paused_by_obstacle'
    PAUSED_BY_BUTTON = 'paused_by_button'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CarStatus from a JSON string"""
        return cls(json.loads(json_str))


