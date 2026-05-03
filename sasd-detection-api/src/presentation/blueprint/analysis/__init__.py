"""
Module level export for analysis blueprint
"""
from flask import Blueprint
from flask_pydantic_spec import FlaskPydanticSpec

analysis_bp = Blueprint(
    name="analysis_bp",
    import_name=__name__,
    url_prefix="/analysis"
)

_analysis_spec = FlaskPydanticSpec(
    backend_name="sasd-detection-api",
    title="sasd-detection-api-spec",
    version="0.1.0"
)
