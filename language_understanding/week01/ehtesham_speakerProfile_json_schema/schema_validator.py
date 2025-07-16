import json
from jsonschema import validate, ValidationError

# Load schema
with open("speaker_profile_schema.json") as schema_file:
    schema = json.load(schema_file)

# Load example profile
with open("speaker_profile_1.json") as data_file:
    profile = json.load(data_file)

# Validate
try:
    validate(instance=profile, schema=schema)
    print("Profile is valid!")
except ValidationError as e:
    print("Validation Error:", e)
