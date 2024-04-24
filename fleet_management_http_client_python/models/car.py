# coding: utf-8

"""
    BringAuto Fleet Management v2 API

    Specification for BringAuto fleet backend HTTP API

    The version of the OpenAPI document: 2.3.1
    Contact: fleet@bringauto.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fleet_management_http_client_python.models.car_state import CarState
from fleet_management_http_client_python.models.mobile_phone import MobilePhone
from typing import Optional, Set
from typing_extensions import Self

class Car(BaseModel):
    """
    Car model structure.
    """ # noqa: E501
    id: Optional[StrictInt] = None
    platform_hw_id: StrictInt = Field(alias="platformHwId")
    name: StrictStr
    car_admin_phone: MobilePhone = Field(alias="carAdminPhone")
    default_route_id: Optional[StrictInt] = Field(default=None, alias="defaultRouteId")
    under_test: Optional[StrictBool] = Field(default=True, alias="underTest")
    last_state: Optional[CarState] = Field(default=None, alias="lastState")
    __properties: ClassVar[List[str]] = ["id", "platformHwId", "name", "carAdminPhone", "defaultRouteId", "underTest", "lastState"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Car from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of car_admin_phone
        if self.car_admin_phone:
            _dict['carAdminPhone'] = self.car_admin_phone.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_state
        if self.last_state:
            _dict['lastState'] = self.last_state.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Car from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "platformHwId": obj.get("platformHwId"),
            "name": obj.get("name"),
            "carAdminPhone": MobilePhone.from_dict(obj["carAdminPhone"]) if obj.get("carAdminPhone") is not None else None,
            "defaultRouteId": obj.get("defaultRouteId"),
            "underTest": obj.get("underTest") if obj.get("underTest") is not None else True,
            "lastState": CarState.from_dict(obj["lastState"]) if obj.get("lastState") is not None else None
        })
        return _obj


