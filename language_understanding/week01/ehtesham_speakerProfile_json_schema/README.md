# Speaker Profile JSON Schema – Project NEXI

---

## 📌 Assigned Task

**Engineer:** M Ehtesham Ul Hassan Malik  
**Task Title:** Speaker Profile JSON Schema  
**Goal:** Define a schema to capture speaker attributes like name, age, gender, mood, language, and education level  
**Deadline:** 19/07/2025 (Saturday)

---

## 📝 Task Description

Design a JSON schema for defining and validating speaker profiles. This data will be used by Nexi’s AI/ML module to adapt responses based on individual speaker characteristics.

---

## ✅ Deliverables

| File | Description |
|------|-------------|
| `speaker_profile_schema.json` | JSON Schema defining valid speaker fields and their data types |
| `speaker_profile_1.json` | First sample speaker profile (valid instance) |
| `speaker_profile_2.json` | Second sample speaker profile (valid instance) |
| `schema_validator.py` | Python script to validate JSON profiles using the defined schema |

---

## Schema Fields

- `name`: Full name of the speaker (string)
- `age`: Age in years (integer)
- `gender`: Enum value (`"male"`, `"female"`, `"other"`)
- `mood`: Enum value (`"happy"`, `"sad"`, `"neutral"`, etc.)
- `education_level`: Enum (`"primary"`, `"secondary"`, `"graduate"`, `"postgraduate"`, `"uneducated"`)
- `language`: Enum (`"english"`, `"urdu"`)

---

## 🛠️ Tools & Resources

- ✅ [https://jsonschema.net](https://jsonschema.net) – Auto-generate and validate JSON Schema
- ✅ `jsonschema` Python library – Programmatic validation
- ✅ VS Code / JSONLint – Formatting and testing

---

## Validation Script

`schema_validator.py` loads the schema and profile, then validates:

```python
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
```

## Outcome

- Created and validated JSON Schema for consistent speaker profiling
- Supports Nexi’s smart response engine based on age, education, and emotion
- Ready to scale and integrate into user profiling modules


## Task Report Summary

### How I Completed the Task:

- Defined schema using jsonschema.net and refined in VS Code.
- Used real-world speaker examples to create 2 valid profiles.
- Built a validator script in Python for ongoing schema testing.

### Tools & Resources Used:
- jsonschema.net
- VS Code
- Python 3
- jsonschema
- library
- JSONLint

### My Approach:
- Iterative testing and validation for accurate field handling.
- Ensured reusability and adaptability by using enums and constraints.
- Validated both schema and instances using code and online tools.

