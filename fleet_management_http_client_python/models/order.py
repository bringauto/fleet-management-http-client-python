# coding: utf-8

"""
    BringAuto Fleet Management v2 API

    Specification for BringAuto fleet backend HTTP API

    The version of the OpenAPI document: 3.0.1
    Contact: fleet@bringauto.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from fleet_management_http_client_python.models.mobile_phone import MobilePhone
from fleet_management_http_client_python.models.order_state import OrderState
from typing import Optional, Set
from typing_extensions import Self

class Order(BaseModel):
    """
    Order object structure.
    """ # noqa: E501
    id: Optional[StrictInt] = None
    priority: Optional[Annotated[str, Field(strict=True)]] = Field(default='normal', description="Priority (low, normal, high)")
    user_id: StrictInt = Field(alias="userId")
    timestamp: Optional[StrictInt] = Field(default=None, description="A Unix timestamp in milliseconds. The timestamp is used to determine the time of creation of an object.")
    car_id: StrictInt = Field(alias="carId")
    notification: Optional[StrictStr] = None
    target_stop_id: StrictInt = Field(alias="targetStopId")
    stop_route_id: StrictInt = Field(alias="stopRouteId")
    notification_phone: Optional[MobilePhone] = Field(default=None, alias="notificationPhone")
    last_state: Optional[OrderState] = Field(default=None, alias="lastState")
    __properties: ClassVar[List[str]] = ["id", "priority", "userId", "timestamp", "carId", "notification", "targetStopId", "stopRouteId", "notificationPhone", "lastState"]

    @field_validator('priority')
    def priority_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(low|normal|high)$", value):
            raise ValueError(r"must validate the regular expression /^(low|normal|high)$/")
        return value

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
        """Create an instance of Order from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of notification_phone
        if self.notification_phone:
            _dict['notificationPhone'] = self.notification_phone.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_state
        if self.last_state:
            _dict['lastState'] = self.last_state.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Order from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "priority": obj.get("priority") if obj.get("priority") is not None else 'normal',
            "userId": obj.get("userId"),
            "timestamp": obj.get("timestamp"),
            "carId": obj.get("carId"),
            "notification": obj.get("notification"),
            "targetStopId": obj.get("targetStopId"),
            "stopRouteId": obj.get("stopRouteId"),
            "notificationPhone": MobilePhone.from_dict(obj["notificationPhone"]) if obj.get("notificationPhone") is not None else None,
            "lastState": OrderState.from_dict(obj["lastState"]) if obj.get("lastState") is not None else None
        })
        return _obj


