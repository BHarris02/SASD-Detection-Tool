"""
Simple utility functions to "serialize" domain objects to dicts.
"""
from dataclasses import asdict, fields
from enum import Enum

from domain.common.result import Result

def _serialize(obj) -> dict:
    return asdict(obj, dict_factory=lambda items: {
        k: v.value if isinstance(v, Enum) else v
        for k, v in items
    })

def serialize_result(result: Result) -> tuple[dict, int]:
    if not result.success:
        return {"error": str(result.error)}, 500

    value = result.value
    if isinstance(value, list):
        return {"result": [_serialize(item) for item in value]}, 200
    return {"result": _serialize(value)}, 200