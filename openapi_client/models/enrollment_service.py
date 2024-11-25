# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from openapi_client.models.enrollment_service_auth import EnrollmentServiceAuth
from openapi_client.models.enrollment_service_service import EnrollmentServiceService
from typing import Optional, Set
from typing_extensions import Self

class EnrollmentService(BaseModel):
    """
    EnrollmentService
    """ # noqa: E501
    authentication: EnrollmentServiceAuth
    service: EnrollmentServiceService
    enrollment_ui_endpoint: StrictStr = Field(alias="enrollment-ui-endpoint")
    __properties: ClassVar[List[str]] = ["authentication", "service", "enrollment-ui-endpoint"]

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
        """Create an instance of EnrollmentService from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of authentication
        if self.authentication:
            _dict['authentication'] = self.authentication.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service
        if self.service:
            _dict['service'] = self.service.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EnrollmentService from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authentication": EnrollmentServiceAuth.from_dict(obj["authentication"]) if obj.get("authentication") is not None else None,
            "service": EnrollmentServiceService.from_dict(obj["service"]) if obj.get("service") is not None else None,
            "enrollment-ui-endpoint": obj.get("enrollment-ui-endpoint")
        })
        return _obj

