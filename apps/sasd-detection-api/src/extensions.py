"""
src/extensions.py
"""
from flask_pydantic_spec import FlaskPydanticSpec

app_spec = FlaskPydanticSpec(
    backend_name="sasd-detection-api",
    version="0.1.0-SNAPSHOT"
)
