# coding: utf-8

"""
    BringAuto Fleet Management v2 API

    Specification for BringAuto fleet backend HTTP API

    The version of the OpenAPI document: 3.4.4
    Contact: fleet@bringauto.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class CarActionStatus(str, Enum):
    """
    Car Action Status enum
    """

    """
    allowed enum values
    """
    NORMAL = 'normal'
    PAUSED = 'paused'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CarActionStatus from a JSON string"""
        return cls(json.loads(json_str))


