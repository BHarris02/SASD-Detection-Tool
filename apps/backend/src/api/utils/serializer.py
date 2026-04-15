"""
Simple utility function to "serialize" domain objects to dicts.
"""
from dataclasses import asdict
from enum import Enum

from domain.common.result import Result

def _parse_obj_to_dict(obj: object) -> dict[str, str]:
    """
    Parse an `object` to dictionary, checking for `Enum` types specifically.
    """
    return asdict(obj, dict_factory=lambda items: {
        key: val.value if isinstance(val, Enum) else val
        for key, val in items
    })

def serialize(result: Result) -> dict[str, str]:
    """
    Serialize a `domain` object to a dict for jsonification.
    """
    if not result.success:
        return {
            "error": f"{result.error}"
        }, 500
    
    value = result.value
    if isinstance(value, list):
        return {
            "response": [ _parse_obj_to_dict(obj) for obj in value ]
        }, 200
    
    return {
        "response": _parse_obj_to_dict(value)
    }
