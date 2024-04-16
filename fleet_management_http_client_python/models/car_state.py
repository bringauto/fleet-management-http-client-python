# coding: utf-8

"""
    BringAuto Fleet Management v2 API

    Specification for BringAuto fleet backend HTTP API

    The version of the OpenAPI document: 2.1.0
    Contact: fleet@bringauto.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from fleet_management_http_client_python.models.car_status import CarStatus
from fleet_management_http_client_python.models.gnss_position import GNSSPosition
from typing import Optional, Set
from typing_extensions import Self

class CarState(BaseModel):
    """
    Car State object structure
    """ # noqa: E501
    id: Optional[StrictInt] = None
    timestamp: Optional[StrictInt] = Field(default=None, description="A Unix timestamp in milliseconds. The timestamp is used to determine the time of creation of an object.")
    status: CarStatus
    fuel: Optional[StrictInt] = 0
    car_id: StrictInt = Field(alias="carId")
    speed: Optional[Union[StrictFloat, StrictInt]] = 0.0
    position: Optional[GNSSPosition] = None
    __properties: ClassVar[List[str]] = ["id", "timestamp", "status", "fuel", "carId", "speed", "position"]

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
        """Create an instance of CarState from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of position
        if self.position:
            _dict['position'] = self.position.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CarState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "timestamp": obj.get("timestamp"),
            "status": obj.get("status"),
            "fuel": obj.get("fuel") if obj.get("fuel") is not None else 0,
            "carId": obj.get("carId"),
            "speed": obj.get("speed") if obj.get("speed") is not None else 0.0,
            "position": GNSSPosition.from_dict(obj["position"]) if obj.get("position") is not None else None
        })
        return _obj


