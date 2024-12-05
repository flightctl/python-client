# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class DeviceLifecycleHookType(str, Enum):
    """
    DeviceLifecycleHookType
    """

    """
    allowed enum values
    """
    BEFOREUPDATING = 'BeforeUpdating'
    AFTERUPDATING = 'AfterUpdating'
    BEFOREREBOOTING = 'BeforeRebooting'
    AFTERREBOOTING = 'AfterRebooting'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DeviceLifecycleHookType from a JSON string"""
        return cls(json.loads(json_str))

