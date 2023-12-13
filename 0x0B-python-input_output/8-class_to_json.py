#!/usr/bin/python3
"""
No module is Imported
"""
def class_to_json(obj):
    if isinstance(obj, dict):
        return (dict{key: class_to_json(value) for key, value in obj.items()})
    else:
        return (dict(obj))
