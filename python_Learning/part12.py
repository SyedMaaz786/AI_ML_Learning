import json

py_obj = {
    "student": {
        "name": "Maaz",
        "age": 22,
        "city": "Hyderabad"
    },

    "numbers": [10, 20, 30, 40, 50],

    "employees": [
        {"id": 1, "name": "Maaz", "role": "Developer"},
        {"id": 2, "name": "Irfan", "role": "Designer"},
        {"id": 3, "name": "Rizwan", "role": "Tester"}
    ]
}

# Convert PYTHON → JSON STRING 

json_str = json.dumps(py_obj)               # Convert dictionary to JSON string
print(type(json_str), "\n", json_str, "\n")

# Convert JSON STRING → PYTHON DICTIONARY

py_loaded = json.loads(json_str)            # Convert JSON string back to dictionary
print(type(py_loaded), "\n", py_loaded, "\n")

