# coding: utf-8

"""
    BringAuto Fleet Management v2 API

    Specification for BringAuto fleet backend HTTP API

    The version of the OpenAPI document: 4.1.2
    Contact: fleet@bringauto.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from fleet_management_http_client_python.models.gnss_position import GNSSPosition
from typing import Optional, Set
from typing_extensions import Self

class RouteVisualization(BaseModel):
    """
    Route Visualization object structure.
    """ # noqa: E501
    id: Optional[StrictInt] = None
    route_id: StrictInt = Field(alias="routeId")
    hexcolor: Optional[Annotated[str, Field(strict=True)]] = Field(default='#FF0000', description="Color in hexadecimal format.")
    points: List[GNSSPosition]
    __properties: ClassVar[List[str]] = ["id", "routeId", "hexcolor", "points"]

    @field_validator('hexcolor')
    def hexcolor_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$", value):
            raise ValueError(r"must validate the regular expression /^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/")
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
        """Create an instance of RouteVisualization from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in points (list)
        _items = []
        if self.points:
            for _item in self.points:
                if _item:
                    _items.append(_item.to_dict())
            _dict['points'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RouteVisualization from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "routeId": obj.get("routeId"),
            "hexcolor": obj.get("hexcolor") if obj.get("hexcolor") is not None else '#FF0000',
            "points": [GNSSPosition.from_dict(_item) for _item in obj["points"]] if obj.get("points") is not None else None
        })
        return _obj


