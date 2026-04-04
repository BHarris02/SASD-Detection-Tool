"""
A generic domain result class returned by interactors.
"""
from dataclasses import dataclass
from typing import Optional

from apps.backend.src.domain.common.error import DomainError

@dataclass
class Result[T]:
    """
    Domain result class returned by interactors.
    """
    success: bool
    value: Optional[T]
    error: Optional[DomainError] = None
