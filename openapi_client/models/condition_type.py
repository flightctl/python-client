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


class ConditionType(str, Enum):
    """
    ConditionType
    """

    """
    allowed enum values
    """
    APPROVED = 'Approved'
    DENIED = 'Denied'
    FAILED = 'Failed'
    ACCESSIBLE = 'Accessible'
    RESOURCEPARSED = 'ResourceParsed'
    SYNCED = 'Synced'
    OVERLAPPINGSELECTORS = 'OverlappingSelectors'
    VALID = 'Valid'
    UPDATING = 'Updating'
    SPECVALID = 'SpecValid'
    MULTIPLEOWNERS = 'MultipleOwners'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConditionType from a JSON string"""
        return cls(json.loads(json_str))

